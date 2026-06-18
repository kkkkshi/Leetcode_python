# 121. Best Time to Buy and Sell Stock

# brute force Approach
# Time: O(n^2)
# Space: O(1)
# 2023.06.23: yes
# notes: check every buy/sell pair and keep the largest difference
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit


# one pass Approach
# Time: O(n)
# Space: O(1)
# 2023.06.23: no
# notes: track the lowest price so far, update profit at each step
class Solution2:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit


# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.28: no
# notes: all stock problems reduce to one DP framework, worth a review
# really strong, I'd honestly call it god-tier
# https://labuladong.github.io/algo/di-er-zhan-a01c6/yong-dong--63ceb/yi-ge-fang-3b01b/
# base case:
# dp[-1][0] = 0
# dp[-1][1] = -infinity
# state transition:
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], - prices[i])
class Solution4:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        for i in range(n):
            if i-1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[n - 1][0]


# Dynamic Programming Space Optimized
# Time: O(n)
# Space: O(1)
# 2023.07.28: no
# notes: same DP but keep only the previous two states, not the table
class Solution5:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        # base case: dp[-1][0] = 0, dp[-1][1] = -infinity
        dp_i_0, dp_i_1 = 0, float('-inf')
        for i in range(n):
            # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp_i_0, dp_i_1 = max(dp_i_0, dp_i_1 + prices[i]), max(dp_i_1, -prices[i])
        return dp_i_0


# Tests:
for sol in (Solution(), Solution2(), Solution4(), Solution5()):
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    assert sol.maxProfit([1, 2, 90, 10, 110]) == 109
