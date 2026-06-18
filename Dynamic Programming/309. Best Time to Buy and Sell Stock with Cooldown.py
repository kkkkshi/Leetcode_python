# 309. Best Time to Buy and Sell Stock with Cooldown

# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.28: yes
# notes: use i-2 for the buy state because of the one-day cooldown
# reference labuladong's unified stock DP framework
# https://labuladong.github.io/algo/di-er-zhan-a01c6/yong-dong--63ceb/yi-ge-fang-3b01b/
# base case:
# dp[-1][0] = dp[...][0] = 0
# dp[-1][1] = dp[...][1] = -infinity
# transition:
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        for i in range(n):
            if i - 1 == -1:
                # base case
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        return dp[n - 1][0]


# Dynamic Programming
# Time: O(n)
# Space: O(1)
# 2023.07.28: yes
# notes: keep one extra previous value to drop the dp array
class Solution2:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp_i_0, dp_i_1, dp_pre_0 = 0, float('-inf'), 0
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp
        return dp_i_0


# Yet-Another Dynamic Programming
# Time: O(n^2)
# Space: O(n)
# 2023.07.28: no
# notes: math-style version, skipped for now
class Solution3:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        L = len(prices)
        # padding the array with additional zero to simply the logic
        MP = [0] * (L + 2)

        for i in range(L-1, -1, -1):
            C1 = 0
            # Case 1). buy and sell the stock
            for sell in range(i + 1, L):
                profit = (prices[sell] - prices[i]) + MP[sell + 2]
                C1 = max(profit, C1)

            # Case 2). do no transaction with the stock p[i]
            C2 = MP[i + 1]

            # sum up two cases
            MP[i] = max(C1, C2)

        return MP[0]


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.maxProfit([1, 2, 3, 0, 2]) == 3
    assert sol.maxProfit([1]) == 0
    assert sol.maxProfit([2, 1]) == 0
    assert sol.maxProfit([1, 2, 4]) == 3
    assert sol.maxProfit([6, 1, 3, 2, 4, 7]) == 6
