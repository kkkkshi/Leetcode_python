# 518. Coin Change II

from functools import cache
from typing import List


# Bottom Up Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: no
# notes: same idea as Solution3, just rewritten bottom up
class Solution:
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coin_len = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(coin_len+1)]
        # dp[i][j]: ways to reach amount j using only the first i coins
        for i in range(1, coin_len+1):
            for j in range(amount+1):
                if j == 0:
                    dp[i][j] = 1
                # if money left is positive, we can take or skip this coin
                elif j - coins[i-1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                # if money left is below 0, we can only skip
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[coin_len][amount]


# Dynamic Programming with Space Optimization
# Time: O(n)
# Space: O(n)
# 2023.07.25: no
# notes: cut the table down to one row
class Solution2:
    def change(self, amount, coins):
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1  # base case
        for i in range(n):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j] + dp[j - coins[i]]
        return dp[amount]


# Top-Down Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.09.03: no
# notes: Sept 3 update:
# 1. no cache here, storing results directly instead
# 2. "i means how many ways the first i coins make amount j" is not
#    quite right; for each new amount we try the first coin, then the
#    second, until the path is blocked, more like backtracking that
#    records results
# 3. if this coin overshoots, try the next; otherwise we can take or
#    skip it, as recorded in the if-else below
# 4. very close to backtracking: i tracks which coin we are on, j
#    tracks how much money is left to break down
class Solution3:
    def change(self, amount, coins):
        def numberOfWays(i, amount):
            if amount == 0:
                return 1
            if i == len(coins):
                return 0
            if memo[i][amount] != -1:
                return memo[i][amount]

            if coins[i] > amount:
                memo[i][amount] = numberOfWays(i + 1, amount)
            else:
                memo[i][amount] = numberOfWays(i, amount - coins[i]) + numberOfWays(i + 1, amount)

            return memo[i][amount]

        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        return numberOfWays(0, amount)


# notes: wrong method; the reason is it is not a plain add/subtract
#        relation, this counts ordered combinations
class Solution4:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for i in range(amount+1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] += dp[i-coin]
        return dp[amount]


# notes: turn the top-down version into backtracking, and back again
class Solution5:
    def change(self, amount, coins):
        @cache
        def numberOfWays(i, amount):
            if amount == 0:
                return 1
            if i == len(coins):
                return 0
            if coins[i] > amount:
                return numberOfWays(i + 1, amount)
            else:
                return numberOfWays(i, amount - coins[i]) + numberOfWays(i + 1, amount)
        return numberOfWays(0, amount)


# Tests:
# Solution4 is the user's documented wrong method (counts permutations),
# so it is left out of the assert loop on purpose.
for sol in (Solution(), Solution2(), Solution3(), Solution5()):
    assert sol.change(5, [1, 2, 5]) == 4
    assert sol.change(3, [2]) == 0
    assert sol.change(10, [10]) == 1
    assert sol.change(0, [7]) == 1
