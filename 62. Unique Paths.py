# 62. Unique Paths

# Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.31: yes
# notes: dp[i][j] is paths to that cell; first row/col are all 1,
#        each other cell sums the cell above and the cell left
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]


# Dynamic Programming
# Time: O(n^2)
# Space: O(n)
# 2023.07.31: yes
# notes: keep only one row; update in place so dp[j] becomes
#        dp[j-1] (left) plus dp[j] (old value above)
class Solution2:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1 for _ in range(n)]
        for i in range(1,m):
            for j in range(1, n):
                dp[j] = dp[j-1]+dp[j]
        return dp[n-1]


# Math
# Time: O((M+N)(log(M+N)loglog(M+N))^2)
# Space: O(1)
# 2023.09.03: no
# notes: pure counting: m-1 moves down, n-1 moves right; the robot
#        only moves right or down, so it is a combination count
from math import factorial
class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(3, 2) == 3
    assert sol.uniquePaths(1, 1) == 1
    assert sol.uniquePaths(1, 10) == 1
