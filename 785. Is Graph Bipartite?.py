# 785. Is Graph Bipartite?

# Depth-First Search Approach
# Time: O(n)
# Space: O(n+e)
# 2023.07.05: yes
# notes: color each node opposite to its neighbor while exploring; if a
#        neighbor already has the same color, it's not bipartite
class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def traverse(graph, node):
            if self.bipartite == False:
                return
            self.visited[node] = True
            for next_node in graph[node]:
                if not self.visited[next_node]:
                    self.color[next_node] = not self.color[node]
                    traverse(graph, next_node)
                else:
                    if self.color[next_node] == self.color[node]:
                        self.bipartite = False
                        return
        self.color = [False]*len(graph)
        self.bipartite = True
        self.visited = [False]*len(graph)
        for i in range(len(graph)):
            traverse(graph, i)
        return self.bipartite


# Tests:
for sol in (Solution(),):
    assert sol.isBipartite([[1,3],[0,2],[1,3],[0,2]]) is True
    assert sol.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]) is False
    assert sol.isBipartite([[1],[0,3],[3],[1,2]]) is True
