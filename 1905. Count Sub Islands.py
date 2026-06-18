# 1905. Count Sub Islands

# BFS Approach
# Time: O(mn)
# Space: O(min(m,n))
# 2023.08.03: yes
# notes: sink every grid2 island that touches water in grid1, then
#        the remaining grid2 islands are all sub-islands; count them
class Solution:
    def countSubIslands(self, grid1, grid2):
        m, n = len(grid1), len(grid1[0])
        # this island can't be a sub-island, so sink it
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    self.dfs(grid2, i, j)

        # every island left in grid2 is a sub-island, count them
        res = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    res += 1
                    self.dfs(grid2, i, j)
        return res

    # from (i, j), turn all connected land into water
    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            return
        if grid[i][j] == 0:
            return

        grid[i][j] = 0
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)


# Tests:
for sol in (Solution(),):
    grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
    grid2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0],
             [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
    assert sol.countSubIslands(grid1, grid2) == 3
    g1 = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]
    g2 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]
    assert sol.countSubIslands(g1, g2) == 2
    assert sol.countSubIslands([[1]], [[0]]) == 0
