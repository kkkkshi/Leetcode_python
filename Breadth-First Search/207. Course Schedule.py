# 207. Course Schedule

from collections import deque


# Depth First Search Approach
# Time: O(m+n)
# Space: O(n)
# 2023.07.04: yes
# notes: DFS each node tracking the current path; if we revisit a
#        node already on the path there is a cycle, so it fails
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def traverse(graph, s):
            if self.onPath[s]:
                self.hasCycle = True
            # visited means we already explored this node and all its
            # descendants, so skip it; also bail out once a cycle is found
            if self.visited[s] or self.hasCycle:
                return
            self.visited[s] = True
            self.onPath[s] = True
            for t in graph[s]:
                traverse(graph, t)
            self.onPath[s] = False

        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
        self.visited = [False] * numCourses
        self.onPath = [False] * numCourses
        self.hasCycle = False
        for i in range(numCourses):
            traverse(graph, i)
        return not self.hasCycle


# Topological Sort Using Kahn's Algorithm Approach
# Time: O(m+n)
# Space: O(m+n)
# 2023.07.04: yes
# notes: repeatedly remove nodes with indegree 0; if we can remove
#        all of them there is no cycle and every course is doable
class Solution2:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        # build the graph
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1
        # find nodes with no indegree and start from them
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        nodesVisited = 0
        while queue:
            node = queue.popleft()
            nodesVisited += 1
            # drop each neighbor's indegree by one; enqueue it at zero
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return nodesVisited == numCourses


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True
    assert sol.canFinish(2, [[1, 0]]) is True
    assert sol.canFinish(2, [[1, 0], [0, 1]]) is False
