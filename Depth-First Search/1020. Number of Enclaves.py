# 1020. Number of Enclaves

from collections import deque


# BFS Approach
# Time: O(mn)
# Space: O(min(m,n))
# 2023.08.03: yes
# notes: flood the land cells touching the border to 0, then the
#        remaining 1s are the enclaves, so just sum them up.
class Solution:
    def bfs(self, x, y, m, n, grid, visit):
        """
        :type x: int
        :type y: int
        :type m: int
        :type n: int
        :type grid: List[List[int]]
        :type visit: List[List[bool]]
        :rtype: None
        """
        q = deque()
        q.append((x, y))
        visit[x][y] = True

        dirx = [0, 1, 0, -1]
        diry = [-1, 0, 1, 0]

        while q:
            temp = q.popleft()
            x, y = temp[0], temp[1]  # row number and column number

            for i in range(4):
                r = x + dirx[i]
                c = y + diry[i]
                if r < 0 or r >= m or c < 0 or c >= n:
                    continue
                elif grid[r][c] == 1 and not visit[r][c]:
                    q.append((r, c))
                    visit[r][c] = True

    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visit = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            # First column.
            if grid[i][0] == 1 and not visit[i][0]:
                self.bfs(i, 0, m, n, grid, visit)
            # Last column.
            if grid[i][n - 1] == 1 and not visit[i][n - 1]:
                self.bfs(i, n - 1, m, n, grid, visit)

        for i in range(n):
            # First row.
            if grid[0][i] == 1 and not visit[0][i]:
                self.bfs(0, i, m, n, grid, visit)
            # Last row.
            if grid[m - 1][i] == 1 and not visit[m - 1][i]:
                self.bfs(m - 1, i, m, n, grid, visit)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visit[i][j]:
                    count += 1

        return count


# DFS Approach
# Time: O(mn)
# Space: O(mn)
# 2023.07.13: yes
# notes: from every border 1, dfs and sink the connected land to 0, then
#        the leftover 1s are enclaves.
class Solution2:
    def numEnclaves(self, grid) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            grid[i][j] = 0
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    dfs(x, y)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    dfs(i, j)
        return sum(sum(row) for row in grid)


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.numEnclaves([[0,0,0,0],
                            [1,0,1,0],
                            [0,1,1,0],
                            [0,0,0,0]]) == 3
    assert sol.numEnclaves([[0,1,1,0],
                            [0,0,1,0],
                            [0,0,1,0],
                            [0,0,0,0]]) == 0
    assert sol.numEnclaves([[0,0,0],
                            [0,1,0],
                            [0,0,0]]) == 1
