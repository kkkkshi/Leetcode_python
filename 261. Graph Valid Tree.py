# 261. Graph Valid Tree

# Depth-First Search Approach
# Time: O(n+e)
# Space: O(n+e)
# 2023.07.06: yes
# notes: DFS from node 0 tracking the current path; revisiting a node
#        on the path means a cycle; a tree must also reach every node
class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        def recursion(node, onPath, parent):
            if node == parent:
                return
            if node in onPath:
                self.cycle = True
            if self.cycle or self.visited[node]:
                return
            onPath.append(node)
            self.visited[node] = True
            for next_node in self.graph[node]:
                if next_node == parent:
                    continue
                recursion(next_node, onPath, node)
            onPath.pop()

        self.graph = [[] for _ in range(n)]
        self.visited = [False] * n
        self.cycle = False
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        recursion(0, [], None)
        return not self.cycle and all(self.visited)


# Depth-First Search Approach (best approach)
# Time: O(n)
# Space: O(n)
# 2023.07.06: no
# notes: with exactly n-1 edges, a plain DFS that reaches all n
#        nodes proves it is a tree; otherwise there is a cycle
class Solution2:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1: return False

        # Create an adjacency list.
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        # We still need a seen set to prevent our code from infinite
        # looping if there *is* cycles (and on the trivial cycles!)
        seen = set()

        def dfs(node):
            if node in seen: return
            seen.add(node)
            for neighbour in adj_list[node]:
                dfs(neighbour)

        dfs(0)
        return len(seen) == n


# Breadth-First Search Approach
# Time: O(n+e)
# Space: O(n+e)
# 2023.07.06: no
# notes: if edge count is not n-1 there is a duplicate edge; track
#        each node's parent so the undirected edge isn't walked back
class Solution3:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # not n-1 edges means there must be a repeated connection
        if len(edges) != n - 1:
            return False
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)
        parent = {0: -1}
        stack = [0]
        while stack:
            node = stack.pop()
            for neighbour in adj_list[node]:
                if neighbour == parent[node]:
                    continue
                if neighbour in parent:
                    return False
                parent[neighbour] = node
                stack.append(neighbour)
        return len(parent) == n


# Breadth-First Search Approach (best approach)
# Time: O(n)
# Space: O(n)
# 2023.07.06: no
# notes: with n-1 edges, BFS that visits all n nodes proves a tree;
#        a tree's BFS never revisits a node, a revisit means a cycle
class Solution4:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1: return False

        # Create an adjacency list.
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        # We still need a seen set to prevent our code from infinite
        # looping if there *is* cycles (and on the trivial cycles!)
        seen = {0}
        stack = [0]

        while stack:
            node = stack.pop()
            for neighbour in adj_list[node]:
                if neighbour in seen:
                    continue
                seen.add(neighbour)
                stack.append(neighbour)

        return len(seen) == n


# Union-Find Approach
# Time: O(n*alpha(n))
# Space: O(n)
# 2023.07.06: yes
# notes: with n-1 edges, union each edge; if a union finds both ends
#        already joined there is a cycle, so it is not a tree
class UnionFind:

    # For efficiency, we aren't using makeset, but instead initialising
    # all the sets at the same time in the constructor.
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        # We use this to keep track of the size of each set.
        self.size = [1] * n

    # The find method, with path compression. There are ways of implementing
    # this elegantly with recursion, but the iterative version is easier for
    # most people to understand!
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # The union method, with optimization union by size. It returns True if a
    # merge happened, False if otherwise.
    def union(self, A, B):
        # Find the roots for A and B.
        root_A = self.find(A)
        root_B = self.find(B)
        # Check if A and B are already in the same set.
        if root_A == root_B:
            return False
        # We want to ensure the larger set remains the root.
        if self.size[root_A] < self.size[root_B]:
            # Make root_B the overall root.
            self.parent[root_A] = root_B
            # The size of the set rooted at B is the sum of the 2.
            self.size[root_B] += self.size[root_A]
        else:
            # Make root_A the overall root.
            self.parent[root_B] = root_A
            # The size of the set rooted at A is the sum of the 2.
            self.size[root_A] += self.size[root_B]
        return True


class Solution5:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # Condition 1: The graph must contain n - 1 edges.
        if len(edges) != n - 1: return False

        # Create a new UnionFind object with n nodes.
        unionFind = UnionFind(n)

        # Add each edge. Check if a merge happened, because if it
        # didn't, there must be a cycle.
        for A, B in edges:
            if not unionFind.union(A, B):
                return False

        # If we got this far, there's no cycles!
        return True


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4(), Solution5()):
    assert sol.validTree(5, [[0,1],[0,2],[0,3],[1,4]]) is True
    assert sol.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]) is False
    assert sol.validTree(4, [[0,1],[2,3]]) is False
    assert sol.validTree(1, []) is True
