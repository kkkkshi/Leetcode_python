# Sorting Approach (best approach)
# Time: O(nlogn)
# Space: O(logn)
# 2023.06.24: yes
# 2023.09.11: update一下，这是9月11日的代码，简洁多了，很棒，我变秃了也变强了
import collections
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: (x[0], x[1]))
        results = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] > results[-1][1]:
                results.append(interval)
            elif interval[0] <= results[-1][1] and interval[1] < results[-1][1]:
                continue
            elif interval[0] <= results[-1][1] and interval[1] > results[-1][1]:
                results[-1][1] = interval[1]
        return results



# Connected Components Approach
# Time: O(n^2)
# Space: O(n^2)
# 2023.06.24: no
# 9月11日 update一下，就是变成图，1. 构建相连节点buildGraph
# 2. getComponents把相邻的节点合并
# 3. mergeNodes输出结果
# 但是真的写的很麻烦，就算用图应该也写不了这么多，无语
class Solution2:
    def overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    def buildGraph(self, intervals):
        graph = collections.defaultdict(list)

        for i, interval_i in enumerate(intervals):
            for j in range(i+1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    graph[tuple(interval_i)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_i)
        return graph

    # merges all of the nodes in this connected component into one interval.
    def mergeNodes(self, nodes):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[1] for node in nodes)
        return [min_start, max_end]

    # gets the connected components of the interval overlap graph.
    def getComponents(self, graph, intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp = collections.defaultdict(list)

        def markComponentDFS(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])

        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if tuple(interval) not in visited:
                markComponentDFS(interval)
                comp_number += 1

        return nodes_in_comp, comp_number


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = self.buildGraph(intervals)
        nodes_in_comp, number_of_comps = self.getComponents(graph, intervals)

        # all intervals in each connected component must be merged.
        return [self.mergeNodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]



# Tests:
intervals = [[8,10],[1,3],[2,6],[15,18]]
intervals2 = [[1,4],[4,5]]
intervals3 = [[1,3]]
test = Solution2()
test.merge(intervals)
test.merge(intervals3)
test.merge(intervals2)