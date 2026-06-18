# 322. Coin Change

# Dynamic programming - Top down
# Time: O(sn)
# Space: O(s)
# 2023.06.21: no
# notes: transition:
# dp = 0, n == 0
#    = -1, n < 0
#    = min(dp(n-coin) + 1)
import math
from functools import lru_cache
from typing import List


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = [-666] * (amount + 1)
        @lru_cache(None)
        def dfs(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if memo[rem] != -666:
                return memo[rem]
            min_cost = float('inf')
            for coin in coins:
                res = dfs(rem - coin)
                if res != -1:
                    min_cost = min(min_cost, res + 1)
            memo[rem] = -1 if min_cost == float('inf') else min_cost
            return memo[rem]
        return dfs(amount)


# Dynamic programming - Bottom up
# Time: O(sn)
# Space: O(n)
# 2023.06.21: no
# notes: both are bottom up; the first loops amount then coins, the
#        second loops coins then amount
class Solution2:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[amount] == float("inf") else dp[amount]


# Dynamic programming - Bottom up
# Time: O(sn)
# Space: O(n)
# notes: loop coins on the outside, amount on the inside
class Solution3:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.coinChange([1, 2, 5], 11) == 3
    assert sol.coinChange([2], 3) == -1
    assert sol.coinChange([1], 0) == 0
    assert sol.coinChange([2, 5, 10, 1], 27) == 4
