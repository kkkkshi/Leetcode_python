# Probability (Math)
# Time: O(n)
# Space: O(1)
# 2023.09.11: no
# notes: 很神奇的数学。。。
# 1. 首先有n个deliver的方法，n的position送货， 一共2n!个选择
# 2. 对于每一个可能，p在d之前有1/2的可能性，所以对于n个p,d,一共是(1/2)^n
# 3. 结果就是(1/2)^n / 2n! 每一步mod即可，防止过大
from functools import cache


class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        ans = 1
        for i in range(1, 2 * n + 1):
            ans = ans * i
            # We only need to divide the result by 2 n-times.
            # To prevent decimal results we divide after multiplying an even number.
            if not i % 2:
                ans = ans // 2
            ans %= MOD
        return ans


# Permutations (Math)
# Time: O(n)
# Space: O(1)
# 2023.09.11: no
# notes: 对于每个p，有n!个方法，对于每个d有1,3,5,7,9...种方法，真不错，应该想不到，对于d值是从后往前
class Solution2:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        ans = 1
        for i in range(1, n + 1):
            # Ways to arrange all pickups, 1*2*3*4*5*...*n
            ans = ans * i
            # Ways to arrange all deliveries, 1*3*5*...*(2n-1)
            ans = ans * (2 * i - 1)
            ans %= MOD
        return ans

# Recursion with Memoization (Top-Down DP)
# Time: O(n^2)
# Space: O(n^2)
# 2023.09.11: no
# notes: 这道题本质上是backtracking优化成的dp，
# 计算一个点的当前方法有两种，1. 当前节点是选择p还是d
# 如果是选择p, waysToPick = unpicked * totalWays(unpicked - 1, undelivered) 传递公式，就是当前的点数+剩下所有为止的可能相乘
# 如果是d, waysToDeliver = (undelivered - unpicked) * totalWays(unpicked, undelivered - 1)，这个稍微有点难理解
# (undelivered - unpicked)代表的是d必须是在有p之后才可以选择d，所有选择d必定是差值，+剩下所有位置可能相乘和p类似
# 注意一点是，对于当前节点p和d是相加关系，并不是相乘关系，是两个分开计算的
# 2. 如果遇到mod = 1_000_000_007的情况，每次加的时候都mod一次即可，不要觉得麻烦，浪费时间复杂度，已经是最省的方法了
class Solution3:
    def countOrders(self, n: int) -> int:
        @cache
        def totalWays(unpicked, undelivered):
            if not unpicked and not undelivered:
                # We have completed all orders.
                return 1
            if (unpicked < 0 or undelivered < 0 or undelivered < unpicked):
                # We can't pick or deliver more than N items
                # Number of deliveries can't exceed number of pickups
                # as we can only deliver after a pickup.
                return 0
            # Count all choices of picking up an order.
            ans = unpicked * totalWays(unpicked - 1, undelivered)  # 转移方程
            ans %= MOD
            # Count all choices of delivering a picked order.
            ans += (undelivered - unpicked) * totalWays(unpicked, undelivered - 1) # 转移方程
            ans %= MOD
            return ans
        MOD = 1_000_000_007
        return totalWays(n, n)


# Bottom Up dp
# Time: O(n^2)
# Space: O(n^2)
# 2023.09.11: no
# notes: 不知道为什么改编没改出来，本质上和上面是一样的，转移方程没写对
# base case我考虑到了，但是这道题转移方程有两个，一个d一个p，相加起来
class Solution4:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        dp = [[0] * (n + 1) for i in range(n + 1)]
        dp[0][0] = 1

        for unpicked in range(n + 1):
            for undelivered in range(unpicked, n + 1):

                # There are some unpicked elements left.
                # We have choice to pick any one of those orders.
                if unpicked > 0:
                    dp[unpicked][undelivered] += unpicked * dp[unpicked - 1][undelivered]
                dp[unpicked][undelivered] %= MOD

                # Number of deliveries done is less than picked orders.
                # We have choice to deliver any one of (undelivered - unpicked) orders.
                if undelivered > unpicked:
                    dp[unpicked][undelivered] += (undelivered - unpicked) * dp[unpicked][undelivered - 1]
                dp[unpicked][undelivered] %= MOD

        return dp[n][n]

# Tests
test = Solution4()
test.countOrders(3)












