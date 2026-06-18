# 122. Best Time to Buy and Sell Stock II

# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.28: yes
# notes: reference the labuladong unified stock framework
# https://labuladong.github.io/algo/di-er-zhan-a01c6/yong-dong--63ceb/yi-ge-fang-3b01b/
# base case:
# dp[-1][0] = dp[...][0] = 0
# dp[-1][1] = dp[...][1] = -infinity
# transition:
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
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
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n - 1][0]


# Dynamic Programming
# Time: O(n)
# Space: O(1)
# 2023.07.28: yes
# notes: same transition collapsed to two rolling variables
class Solution2:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        # base case: dp[-1][0] = 0, dp[-1][1] = -infinity
        dp_i_0, dp_i_1 = 0, float('-inf')
        for i in range(n):
            dp_i_0, dp_i_1 = max(dp_i_0, dp_i_1 + prices[i]), max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0


# Brute force method not listed here

# Peak Valley Approach
# Time: O(n)
# Space: O(1)
# 2023.07.28: yes
# notes: sum each valley-to-peak rise; still O(n) but spends extra
#        time scanning for each local min
class Solution3:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        i = 0
        maxprofit = 0
        while i < n - 1:
            # Find the valley (local minimum)
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            # Find the peak (local maximum)
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            # Calculate the profit and add it to maxprofit
            maxprofit += peak - valley
        return maxprofit


# One Pass Approach
# Time: O(n)
# Space: O(1)
# 2023.07.28: yes
# notes: add every step that goes up versus the previous day
class Solution4:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1]
        return maxprofit


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    assert sol.maxProfit([5]) == 0
