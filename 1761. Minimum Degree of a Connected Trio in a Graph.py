# 1761. Minimum Degree of a Connected Trio in a Graph

# Brute Force
# Time: O(n^3)
# Space: O(n)
# 2023.08.18: yes
# notes: pick any 3 nodes; if they form a trio, the answer is the
#        sum of degrees minus 6, since the 6 inner edges don't count
# no official solution, reference:
# https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/solutions/1204311/python-sorting-degree-with-explanation-details/
from collections import defaultdict
from itertools import combinations


class Solution:
    def minTrioDegree(self, n, edges):
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        min_degree = float('inf')
        for u in range(1, n + 1):
            for v, w in combinations(graph[u], 2):
                if v in graph[w]:
                    min_degree = min(min_degree, len(graph[u]) + len(graph[v]) + len(graph[w]) - 6)
        return min_degree if min_degree != float('inf') else -1


# Brute Force
# Time: O(n^3)
# Space: O(n)
# 2023.08.18: yes
# notes: same idea but optimized; sort by degree and stop early once
#        the current node already exceeds the best possible result
class Solution2:
    def minTrioDegree(self, n, edges):
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        min_degree = float('inf')
        for u in sorted(range(1, n + 1), key=lambda x: len(graph[x])):
            if len(graph[u]) >= min_degree / 3:
                break
            for v in graph[u]:
                for w in graph[v]:
                    if w in graph[u]:
                        min_degree = min(min_degree, len(graph[u]) + len(graph[v]) + len(graph[w]))
        return min_degree - 6 if min_degree != float('inf') else -1


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.minTrioDegree(6, [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]) == 3
    assert sol.minTrioDegree(7, [[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]]) == 0
    assert sol.minTrioDegree(3, [[1, 2]]) == -1
