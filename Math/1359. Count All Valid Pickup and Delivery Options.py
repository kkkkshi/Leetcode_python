# 1359. Count All Valid Pickup and Delivery Options

# Probability (Math)
# Time: O(n)
# Space: O(1)
# 2023.09.11: no
# notes: neat bit of math.
# 1. with n deliveries placed there are (2n)! orderings.
# 2. each pickup is before its delivery with prob 1/2, so over n
#    pairs that is (1/2)^n.
# 3. result is (2n)! * (1/2)^n; mod at every step to avoid overflow.
from functools import cache


class Solution:
    def countOrders(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
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
# notes: each pickup has n! arrangements; each delivery has
#        1,3,5,7,9... slots counting from the back
class Solution2:
    def countOrders(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
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
# notes: backtracking optimized into dp. At each node decide to pick
# or deliver. Picking: waysToPick = unpicked * totalWays(unpicked-1,
# undelivered), the current count times the ways for the rest.
# Delivering: waysToDeliver = (undelivered - unpicked) *
# totalWays(unpicked, undelivered-1); (undelivered - unpicked) is
# because a delivery is only allowed after its pickup, so it equals
# that gap, times the ways for the rest like pickup.
# Note pick and deliver are added, not multiplied; they are computed
# separately.
class Solution3:
    def countOrders(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
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
            ans = unpicked * totalWays(unpicked - 1, undelivered)  # transition
            ans %= MOD
            # Count all choices of delivering a picked order.
            ans += (undelivered - unpicked) * totalWays(unpicked, undelivered - 1) # transition
            ans %= MOD
            return ans
        MOD = 1_000_000_007
        return totalWays(n, n)


# Bottom Up dp
# Time: O(n^2)
# Space: O(n^2)
# 2023.09.11: no
# notes: same as above but iterative; base case is easy, the trick
#        is the two transitions (pick and deliver) added together
class Solution4:
    def countOrders(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
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


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.countOrders(1) == 1
    assert sol.countOrders(2) == 6
    assert sol.countOrders(3) == 90
    assert sol.countOrders(20) == 580270580
