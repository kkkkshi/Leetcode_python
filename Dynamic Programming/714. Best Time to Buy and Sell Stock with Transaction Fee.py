# 714. Best Time to Buy and Sell Stock with Transaction Fee

# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.28: yes
# notes: base case needs -fee, the transition also needs -fee
# reference to labuladong's unified stock framework
# https://labuladong.github.io/algo/di-er-zhan-a01c6/yong-dong--63ceb/yi-ge-fang-3b01b/
# base case:
# dp[-1][0] = dp[...][0] = 0
# dp[-1][1] = dp[...][1] = -infinity
# transition equations:
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        for i in range(n):
            if i - 1 == -1:
                # base case
                dp[i][0] = 0
                dp[i][1] = -prices[i]-fee
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
        return dp[n - 1][0]


# Dynamic Programming
# Time: O(n)
# Space: O(1)
# 2023.07.28: yes
# notes: same recurrence but keep only the two latest states in two
#        rolling variables
class Solution2:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        # base case: dp[-1][0] = 0, dp[-1][1] = -infinity
        dp_i_0, dp_i_1 = 0, float('-inf')-fee
        for i in range(n):
            dp_i_0, dp_i_1 = max(dp_i_0, dp_i_1 + prices[i]), max(dp_i_1, dp_i_0 - prices[i] -fee)
        return dp_i_0


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.maxProfit([1,3,2,8,4,9], 2) == 8
    assert sol.maxProfit([1,3,7,5,10,3], 3) == 6
    assert sol.maxProfit([1], 1) == 0
