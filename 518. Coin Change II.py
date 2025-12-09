# Bottom Up Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: no
# notes: 如Solution3，这个只是改进成bottom up
from functools import cache
from typing import List

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coin_len = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(coin_len+1)]
        # dp[i][j] 只使用前i中coins，有j种方法达到金额
        for i in range(1, coin_len+1):
            for j in range(amount+1):
                if j == 0:
                    dp[i][j] = 1
                # 如果剩余金钱数大于0，可以选择拿或者不拿
                elif j - coins[i-1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                # 剩余金钱数小于0，只能不拿
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[coin_len][amount]

# Dynamic Programming with Space Optimization
# Time: O(n)
# Space: O(n)
# 2023.07.25: no
# notes: 优化空间
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
# notes: 9月3日update一下：
# 1. 这道题没用cache，用的是直接储存的方式
# 2. "这个dp设置真的非常难理解，i代表只用前i中金币到达j金额可以有多少种方法组成方法"这句话其实是有问题的
# 因为每到一个新金额，先试第一个coin，再试第二个coin，直到路径堵死，更像backtracking记录下来
# 3. 如果当前这种金币超额了，就试下一种金额， 否则就可以选择拿或者不拿这枚金币，在下面的if-else有记录
# 4. backtracking 非常像，i记录的是现在到第几种金币了，j记录还有多少钱需要分解掉
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

# notes: 错误方法，理由，并不是单纯的加减关系
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

# notes: 把top-down 改成 backtracking，同时，也可以改回去
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
test = Solution5()
test.change(amount = 5, coins = [1,2,5])