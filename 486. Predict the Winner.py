# 486. Predict the Winner

# Same as Q877 dp solution, not the math solution :)
import collections
from functools import lru_cache


# Top Down Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.27: no
# notes: dp value is the score difference; the first player wants
#        the pile result max, the second wants it min, hence
#        max and min
class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        memo = collections.defaultdict(int)
        def maxDiff(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left == right:
                return nums[left]
            score_by_left = nums[left] - maxDiff(left + 1, right)
            score_by_right = nums[right] - maxDiff(left, right - 1)
            memo[(left, right)] = max(score_by_left, score_by_right)
            return memo[(left, right)]
        return maxDiff(0, n - 1) >= 0


# Bottom Up Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.27: no
# notes: 2D iteration of the transition:
#        nums[left] - dp[left + 1][right]
#        nums[right] - dp[left][right - 1]
class Solution2:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left][right] = max(nums[left] - dp[left + 1][right], nums[right] - dp[left][right - 1])
        return dp[0][n - 1] >= 0


# Bottom Up 1D Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.27: no
# notes: same transition compressed into a 1D rolling array
class Solution3:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = nums[:]
        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left] = max(nums[left] - dp[left + 1], nums[right] - dp[left])
        return dp[0] >= 0


# DIFFERENT DYNAMIC PROGRAMMING SOLUTION - 2D REUCRSION - 1D ITERATION
# Top Down Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.27: no
# notes: https://www.youtube.com/watch?v=WxpIHvsu1RI
#        if you pick one side, the opponent only gets the rest;
#        maximize over picking left or right
class Solution4:
    def PredictTheWinner(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        @lru_cache(None)
        def dp(left, right):
            if left > right:
                return (0, 0)
            pickLeft = dp(left + 1, right)
            pickRight = dp(left, right - 1)
            if piles[left] + pickLeft[1] > piles[right] + pickRight[1]:
                # If the left choice has higher score than the right choice
                return piles[left] + pickLeft[1], pickLeft[0]  # then pick left
            return piles[right] + pickRight[1], pickRight[0]  # else pick right

        alexScore, leeScore = dp(0, len(piles) - 1)
        return alexScore > leeScore


# Bottom Up Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.27: no
# notes: adapted from solution3, traversed diagonally
class Solution5():
    def PredictTheWinner(self, p):
        """
        :type p: List[int]
        :rtype: bool
        """
        n = len(p)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = p[i]
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1])
        return dp[0][-1] > 0


# Bottom Up Dynamic Programming
# Time: O(n^2)
# Space: O(n)
# 2023.07.27: no
# notes: solution4 with the space compressed
class Solution6():
    def PredictTheWinner(self, p):
        """
        :type p: List[int]
        :rtype: bool
        """
        n = len(p)
        dp = p[:]
        for d in range(1, n):
            for i in range(n - d):
                dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i])
        return dp[0] > 0


# Tests:
# Use even-length, tie-free inputs so the >= 0 (Predict the Winner)
# and > 0 (Stone Game) solutions agree.
for sol in (Solution(), Solution2(), Solution3(),
            Solution4(), Solution5(), Solution6()):
    assert sol.PredictTheWinner([1, 5, 2, 4]) is True
    assert sol.PredictTheWinner([5, 3, 4, 5]) is True
    assert sol.PredictTheWinner([1, 5, 233, 7]) is True
    assert sol.PredictTheWinner([3, 9, 1, 2]) is True
