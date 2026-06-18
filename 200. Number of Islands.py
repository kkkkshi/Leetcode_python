# 200. Number of Islands

from collections import deque


# BFS Approach
# Time: O(mn)
# Space: O(min(m,n))
# 2023.07.13: yes
# notes: scan the grid; on an unvisited '1' start a BFS that marks
#        all connected land, counting one island per BFS
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        visited = [[False]*col for _ in range(row)]
        offsets = [[1,0], [0, 1], [-1, 0], [0, -1]]
        q = deque()
        numIslands = 0
        for i in range(row):
            for j in range(col):
                if visited[i][j] == False:
                    visited[i][j] = True
                    if grid[i][j] == "1":
                        q.append([i, j])
                        numIslands += 1
                        while q:
                            cur_row, cur_col = q.popleft()
                            for k in range(len(offsets)):
                                next_row, next_col = cur_row + offsets[k][0], cur_col + offsets[k][1]
                                if next_row < 0 or next_row >= row or next_col < 0 or next_col >= col or visited[next_row][next_col] == True or grid[next_row][next_col] == '0':
                                    continue
                                visited[next_row][next_col] = True
                                q.append([next_row, next_col])
        return numIslands


# DFS Approach
# Time: O(mn)
# Space: O(mn)
# 2023.07.13: yes
# notes: on each '1' sink the whole island by flipping cells to '0'
#        via DFS, counting one island each time a new '1' is hit
class Solution2:
    def dfs(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])
        grid[r][c] = '0'
        if r - 1 >= 0 and grid[r-1][c] == '1':
            self.dfs(grid, r - 1, c)
        if r + 1 < nr and grid[r+1][c] == '1':
            self.dfs(grid, r + 1, c)
        if c - 1 >= 0 and grid[r][c-1] == '1':
            self.dfs(grid, r, c - 1)
        if c + 1 < nc and grid[r][c+1] == '1':
            self.dfs(grid, r, c + 1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nr = len(grid)
        if not nr:
            return 0
        nc = len(grid[0])
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    self.dfs(grid, r, c)
        return num_islands


# Union-Find Approach
# Time: O(mn)
# Space: O(mn)
# 2023.07.13: yes
# notes: union every land cell with its land neighbors; islands left
#        is total cells minus water minus the merges done
class Union_Find:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        self.count -= 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def counts(self):
        return self.count

    def zero(self):
        self.count-= 1


class Solution3:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        total = row * col
        uf = Union_Find(total)
        offsets = [[0,1], [1,0], [0,-1], [-1,0]]
        visited = [[False]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "0":
                    visited[i][j] = True
                    uf.zero()
                    continue
                for k in range(len(offsets)):
                    new_row, new_col = i + offsets[k][0], j + offsets[k][1]
                    if new_row >= 0 and new_row < row and new_col >= 0 and new_col < col:
                        if grid[new_row][new_col] == "1":
                            uf.union(i*col+j, new_row*col+new_col)
                            visited[new_row][new_col] = True
        return uf.counts()


# Tests:
def make_grid(rows):
    return [list(r) for r in rows]


grid1 = ["11000", "11000", "00100", "00011"]
grid2 = ["11110", "11010", "11000", "00000"]
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.numIslands(make_grid(grid1)) == 3
    assert sol.numIslands(make_grid(grid2)) == 1
    assert sol.numIslands(make_grid(["0"])) == 0
