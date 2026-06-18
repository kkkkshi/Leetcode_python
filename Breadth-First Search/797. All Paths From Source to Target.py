# 797. All Paths From Source to Target

from functools import lru_cache


# Backtracking Approach
# Time: O(2^n*n)
# Space: O(n)
# 2023.07.04: yes
# notes: dfs from node 0, extending the current path; on reaching the
#        last node, record a copy of the path
class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def backtracking(node, cur_path):
            if node == target:
                results.append(cur_path[:])
                return
            for next_node in graph[node]:
                cur_path.append(next_node)
                backtracking(next_node, cur_path)
                cur_path.pop()
        target = len(graph)-1
        results = []
        backtracking(0, [0])
        return results


# Top-Down Dynamic Programming Approach
# Time: O(2^n*n)
# Space: O(2^n*n)
# 2023.07.04: no
# notes: same idea as above but memoize the paths from each node, so
#        all_paths_to_target(next_node) reuses cached results
class Solution2:
    def allPathsSourceTarget(self, graph):
        target = len(graph) - 1
        # apply the memoization
        @lru_cache(maxsize=None)
        def all_paths_to_target(curr_node):
            if curr_node == target:
                return [[target]]
            results = []
            for next_node in graph[curr_node]:
                for path in all_paths_to_target(next_node):
                    results.append([curr_node] + path)
            return results
        return all_paths_to_target(0)


# Tests:
for sol in (Solution(), Solution2()):
    assert sorted(sol.allPathsSourceTarget([[1,2],[3],[3],[]])) == [[0,1,3],[0,2,3]]
    assert sorted(sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])) == \
        [[0,1,2,3,4],[0,1,3,4],[0,1,4],[0,3,4],[0,4]]
    assert sol.allPathsSourceTarget([[1],[]]) == [[0,1]]
