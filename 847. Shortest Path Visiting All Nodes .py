# 847. Shortest Path Visiting All Nodes

# DFS + Memoization (Top-Down DP):
# Time: O(2^n*n^2)
# Space: O(2^n*n)
# 2023.09.01: no
# notes: Travelling Salesman style; since n <= 12 brute force works.
#        dp(node, mask) = 1 + min over neighbors of dp on the same
#        mask (revisit) or mask with this node cleared (new node).
#        Seed the cache with infinity to block returning by the path
#        before it is computed.
from typing import List


class Solution:
    def shortestPathLength(self, graph):
        def dp(node, mask):
            state = (node, mask)
            if state in cache:
                return cache[state]
            if mask & (mask - 1) == 0:
                # Base case - mask only has a single "1", which means
                # that only one node has been visited (the current node)
                return 0
            cache[state] = float("inf") # Avoid infinite loop in recursion
            for neighbor in graph[node]:
                if mask & (1 << neighbor):
                    already_visited = 1 + dp(neighbor, mask)
                    not_visited = 1 + dp(neighbor, mask ^ (1 << node))
                    cache[state] = min(cache[state], already_visited, not_visited)
            return cache[state]
        n = len(graph)
        ending_mask = (1 << n) - 1
        cache = {}
        return min(dp(node, ending_mask) for node in range(n))


# BFS:
# Time: O(2^n*n^2)
# Space: O(2^n*n)
# 2023.09.03: no
# notes: state is (node, mask) of nodes seen on the way here; that mask
#        is the path. Expand level by level, each layer adds one step.
class Solution2:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0

        n = len(graph)
        ending_mask = (1 << n) - 1
        queue = [(node, 1 << node) for node in range(n)]
        seen = set(queue)

        steps = 0
        while queue:
            next_queue = []
            for i in range(len(queue)):
                node, mask = queue[i]
                for neighbor in graph[node]:
                    next_mask = mask | (1 << neighbor)
                    if next_mask == ending_mask:
                        return 1 + steps

                    if (neighbor, next_mask) not in seen:
                        seen.add((neighbor, next_mask))
                        next_queue.append((neighbor, next_mask))

            steps += 1
            queue = next_queue


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.shortestPathLength([[1, 2, 3], [0], [0], [0]]) == 4
    assert sol.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]) == 4
    assert sol.shortestPathLength([[0]]) == 0
