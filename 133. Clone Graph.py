# 133. Clone Graph

from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build(adj):
    # adj is 1-indexed adjacency list, adj[i] = neighbors of node i+1
    if not adj:
        return None
    nodes = {i: Node(i) for i in range(1, len(adj) + 1)}
    for i, neighbors in enumerate(adj, start=1):
        nodes[i].neighbors = [nodes[j] for j in neighbors]
    return nodes[1]


def to_adj(node):
    # serialize a graph back into a 1-indexed adjacency list
    if not node:
        return []
    seen = {}
    queue = deque([node])
    seen[node.val] = node
    while queue:
        cur = queue.popleft()
        for nb in cur.neighbors:
            if nb.val not in seen:
                seen[nb.val] = nb
                queue.append(nb)
    return [[nb.val for nb in seen[v].neighbors]
            for v in sorted(seen)]


# BFS Approach (best approach)
# Time: O(n+m)
# Space: O(n)
# 2023.07.13: yes
# notes: BFS the graph, cloning each node on first visit and
#        wiring up the cloned neighbors as we go
class Solution:
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        visited = {}
        q = deque([node])
        visited[node] = Node(node.val, [])
        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]


# DFS Approach (best approach)
# Time: O(n+m)
# Space: O(n)
# 2023.07.13: yes
# notes: recurse, cloning each node once via a visited map and
#        cloning its neighbors recursively
class Solution2:
    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone_node


# Tests:
for sol in (Solution(), Solution2()):
    adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
    assert to_adj(sol.cloneGraph(build(adj))) == adj
    assert to_adj(sol.cloneGraph(build([[]]))) == [[]]
    assert to_adj(sol.cloneGraph(build([]))) == []
