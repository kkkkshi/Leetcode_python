# 210. Course Schedule II

from collections import deque, defaultdict


# Using Node Indegree Approach
# Time: O(v+e)
# Space: O(v+e)
# 2023.07.04: yes
# notes: Kahn's algorithm; keep taking nodes with indegree 0 in order
#        and decrementing neighbors; empty result means a cycle
class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for i in prerequisites:
            graph[i[1]].append(i[0])
            indegree[i[0]] += 1
        self.onPath = []
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            self.onPath.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(self.onPath) == numCourses:
            return self.onPath
        return []


# Using Depth First Search Approach
# Time: O(v+e)
# Space: O(v+e)
# 2023.07.04: no
# notes: DFS coloring nodes; an edge to a GRAY (in-progress) node is
#        a cycle; push nodes post-order and reverse for the order
class Solution2:

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)

        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True

        # By default all vertces are WHITE
        color = {k: Solution2.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return

            # Start the recursion
            color[node] = Solution2.GRAY

            # Traverse on neighboring vertices
            # white = unseen, keep going; gray = a cycle; black = done,
            # already processed so it has no effect
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution2.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution2.GRAY:
                         # An edge to a GRAY vertex represents a cycle
                        is_possible = False

            # Recursion ends. We mark it as black
            color[node] = Solution2.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution2.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []


# Tests:
def is_valid_order(order, numCourses, prerequisites):
    if len(order) != numCourses:
        return False
    pos = {c: i for i, c in enumerate(order)}
    for after, before in prerequisites:
        if pos[before] > pos[after]:
            return False
    return True


for sol in (Solution(), Solution2()):
    p1 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    assert is_valid_order(sol.findOrder(4, p1), 4, p1)
    assert sol.findOrder(2, [[1, 0]]) == [0, 1]
    assert sol.findOrder(1, []) == [0]
    assert sol.findOrder(2, [[0, 1], [1, 0]]) == []
