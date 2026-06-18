# 64. Minimum Path Sum

# Dynamic Programming 2D recursion
# Time: O(mn)
# Space: O(mn)
# 2023.07.26: yes
# notes: top-down dp(i, j) = grid[i][j] plus the cheaper of the cell
#        above and the cell to the left, memoized
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # memo table, all cells start at -1
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        def dp(i, j):
            # base case
            if i == 0 and j == 0:
                return grid[0][0]
            if i < 0 or j < 0:
                return float('inf')
            # avoid recomputing
            if memo[i][j] != -1:
                return memo[i][j]
            # store the computed result in the memo
            memo[i][j] = min(
                dp(i - 1, j),
                dp(i, j - 1)
            ) + grid[i][j]

            return memo[i][j]

        return dp(m - 1, n - 1)


# Dynamic Programming 2D iteration
# Time: O(mn)
# Space: O(mn)
# 2023.07.26: yes
# notes: fill the first row and column by prefix sums, then each cell
#        adds the cheaper of its top and left neighbor
class Solution2:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]


# Dynamic Programming 1D Iteration
# Time: O(mn)
# Space: O(min(m,n))
# 2023.07.26: yes
# notes: keep one row; dp[j] holds the row above, dp[j-1] the left
#        cell, so update dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
class Solution3:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [0 for _ in range(n)]
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[n-1]


# Dynamic Programming No extra space
# Time: O(mn)
# Space: O(1)
# 2023.07.26: yes
# notes: edit the grid in place, walking from bottom-right; some say
#        mutating the input is not ideal but it works
class Solution4:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 and j != cols - 1:
                    grid[i][j] += grid[i][j + 1]
                elif j == cols - 1 and i != rows - 1:
                    grid[i][j] += grid[i + 1][j]
                elif i != rows - 1 and j != cols - 1:
                    grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7
    assert sol.minPathSum([[1,2,3],[4,5,6]]) == 12
    assert sol.minPathSum([[5]]) == 5
    assert sol.minPathSum([[1,2],[1,1]]) == 3
