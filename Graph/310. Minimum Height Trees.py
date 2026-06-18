# 310. Minimum Height Trees

# Breadth-First Search Approach
# Time: O(v)
# Space: O(v)
# 2023.07.14: yes
# notes: trim leaves layer by layer; the last 1 or 2 nodes left are
#        the centroids that give the minimum height
class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # edge cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves


# Tests:
for sol in (Solution(),):
    assert sorted(sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])) == [1]
    assert sorted(sol.findMinHeightTrees(
        6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])) == [3, 4]
    assert sorted(sol.findMinHeightTrees(1, [])) == [0]
    assert sorted(sol.findMinHeightTrees(2, [[0, 1]])) == [0, 1]
