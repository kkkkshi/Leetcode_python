# 877. Stone Game

# Dynamic Programming 1D recursion
# Time: O(mn)
# Space: O(m)
# 2023.07.27: no
# notes: with an even number of piles and an odd total, the first player
#        can always win, so the answer is just True.
from functools import lru_cache


class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return True


# Top Down Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.27: no
# notes: dp(i, j) is the score difference (current player minus the other)
#        on piles[i..j]; first player maximizes, second player minimizes.
class Solution2:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        N = len(piles)
        @lru_cache(None)
        def dp(i, j):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j: return 0
            parity = (j - i - N) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
            else:
                return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

        return dp(0, N - 1) > 0


# Top Down Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.27: no
# notes: https://www.youtube.com/watch?v=WxpIHvsu1RI
#        dp returns (my best, opponent best) on a range; take whichever end
#        leaves you the larger score, the opponent then plays the rest.
class Solution3:
    def stoneGame(self, piles):
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
# notes: same score-difference dp as solution3, filled iteratively by
#        increasing range length (diagonal sweep).
class Solution4():
    def stoneGame(self, p):
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
# notes: solution4 with the 2D table squeezed into one row.
class Solution5:
    def stoneGame(self, p):
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
for sol in (Solution(), Solution2(), Solution3(), Solution4(), Solution5()):
    assert sol.stoneGame([5, 3, 4, 5]) is True
    assert sol.stoneGame([3, 7, 2, 3]) is True
    assert sol.stoneGame([1, 2]) is True
