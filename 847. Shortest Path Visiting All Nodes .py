# DFS + Memoization (Top-Down DP):
# Time: O(2^n*n^2)
# Space: O(2^n*n)
# 2023.09.01: no
# notes: Travelling Sailing Problem
# 因为n<=12，所以可以用暴力解
# dp等式： dp(node, mask) = 1 + min(dp(neighbor, mask), dp(neighbor, mask ^ (1 << node))), for all neighbors in graph[node]
# 下一步有两个状态，回到之前走过的点，或者去一个新的点，对应的就是，bitmask不变或者bitmask变化一位
# infinite的意义是防止在还没cahce[state]之前就调用了，防止返回原路的可能
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


# BFS :
# Time: O(2^n*n^2)
# Space: O(2^n*n)
# 2023.09.03: no
# notes: seen是见过的可能性(node, mask)，当前节点以其当前节点已经遇到的所有的点，就是存储的路径
# 把当前节点和当前路径存储，并且拓展一次step就+1即可
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
test = Solution2()
test.shortestPathLength(graph = [[1,2,3],[0],[0],[0]])