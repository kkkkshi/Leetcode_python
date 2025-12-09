# DFS
# Time: O(n^2)
# Space: O(n)
# 2023.10.31: no
# notes: dfs遍历，根据顺序遍历每一条边，遇到就加到set里，并确认是不是有环
import collections
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graphs = collections.defaultdict(list)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                for neighbor in graphs[source]:
                    if dfs(neighbor, target):
                        return True
                return False

        for edge in edges:
            seen = set()
            if edge[0] in graphs and edge[1] in graphs and dfs(edge[0], edge[1]):
                return edge
            graphs[edge[0]].append(edge[1])
            graphs[edge[1]].append(edge[0])


# Union-Find
# Time: O(n)
# Space: O(n)
# 2023.10.31: no
# notes: 常规union-find
class Union_Find:
    def __init__(self):
        self.parent = list(range(1001))
        self.size = [1]*1001

    def union(self, p, q):
        p_parent, q_parent = self.find(p), self.find(q)
        if p_parent == q_parent:
            return True
        elif self.size[p_parent] < self.size[q_parent]:
            self.parent[p_parent] = q_parent
            self.size[q_parent] += self.size[p_parent]
        else:
            self.parent[q_parent] = p_parent
            self.size[p_parent] += self.size[q_parent]
        return False

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

class Solution2:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = Union_Find()
        for edge in edges:
            if uf.union(edge[0], edge[1]):
                return edge

# Tests:
test = Solution2()
test.findRedundantConnection(edges=[[1, 2], [1, 3], [2, 3]])



