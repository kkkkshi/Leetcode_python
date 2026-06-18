# 70. Climbing Stairs

import math


# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.31: yes
# notes: dp[i] = dp[i-1] + dp[i-2], ways to reach step i
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]


# Dynamic Programming
# Time: O(n)
# Space: O(1)
# 2023.07.31: yes
# notes: roll only the last two values instead of a full dp array
class Solution2:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp_0, dp_1 = 1, 1
        for i in range(2, n+1):
            dp_2 = dp_0 + dp_1
            dp_0, dp_1 = dp_1, dp_2
        return dp_1


# Fibonacci Number
# Time: O(logn)
# Space: O(1)
# 2023.07.31: no
# notes: closed-form Binet formula for the Fibonacci number
class Solution3:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        return int((math.pow(phi, n + 1) - math.pow(psi, n + 1)) / sqrt5)


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(4) == 5
    assert sol.climbStairs(1) == 1
