# 887. Super Egg Drop

# Top Down Dynamic Programming (times out)
# Time: O(kn^2)
# Space: O(kn)
# 2023.07.27: no
# notes: dp(K, N) is the fewest drops needed for N floors with K eggs.
#        base cases: N == 0 needs 0 drops, K == 1 must scan linearly (N).
#        try every floor and take the worst of break / no-break.
class Solution:
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # Memoization table
        memo = [[-666 for _ in range(N + 1)] for _ in range(K + 1)]
        return self.dp(K, N, memo)

    def dp(self, K, N, memo):
        # Base cases
        if K == 1:
            return N
        if N == 0:
            return 0

        # Check memoization table to avoid redundant calculations
        if memo[K][N] != -666:
            return memo[K][N]

        # State transition
        res = float('inf')
        for i in range(1, N + 1):
            # Try all floors and take the minimum attempts needed
            res = min(
                res,
                # Take the worst case scenario between egg breaks and doesn't break
                max(self.dp(K, N - i, memo), self.dp(K - 1, i - 1, memo)) + 1
            )

        # Store result in memoization table
        memo[K][N] = res
        return res


# Top down Dynamic Programming with Binary Search
# Time: O(knlogn)
# Space: O(kn)
# 2023.07.27: no
# notes: res = min(res, max(dp(K, N-i), dp(K-1, i-1)) + 1); the break and
#        no-break curves cross, so binary search the floor instead of scan.
class Solution2:
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # Memoization table
        memo = [[-666 for _ in range(N + 1)] for _ in range(K + 1)]
        return self.dp(K, N, memo)

    def dp(self, K, N, memo):
        # Base cases
        if K == 1:
            return N
        if N == 0:
            return 0

        # Check memoization table to avoid redundant calculations
        if memo[K][N] != -666:
            return memo[K][N]

        # Binary search for optimal floor to drop the egg
        res = float('inf')
        lo, hi = 1, N
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            # Check both cases when the egg breaks and when it doesn't break
            broken = self.dp(K - 1, mid - 1, memo)
            not_broken = self.dp(K, N - mid, memo)
            # res = min(max(break, no break) + 1)
            if broken > not_broken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, not_broken + 1)

        # Store result in memoization table
        memo[K][N] = res
        return res


# Bottom Up Dynamic Programming
# Time: O(knlogn)
# Space: O(kn)
# 2023.07.27: no
# notes: flip the state: dp[k][m] is the most floors coverable with k eggs
#        in m drops, dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1 (above floors
#        + below floors + the current one); grow m until it covers N.
class Solution3:
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # Create the dp array (2D table)
        dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

        # Base cases (already initialized as 0 in Python)
        # dp[0][..] = 0
        # dp[..][0] = 0

        m = 0
        # grow m until dp covers N floors
        while dp[K][m] < N:
            m += 1
            for k in range(1, K + 1):
                dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1

        return m


# Dynamic Programming with Optimality Criterion
# Time: O(kn)
# Space: O(kn)
# 2023.07.27: no
# notes: same recurrence as solution3 but reuse the monotonic optimal
#        floor x across n so it never moves backward, dropping a log factor.
class Solution4:
    def superEggDrop(self, K: int, N: int) -> int:
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # Right now, dp[i] represents dp(1, i)
        dp = range(N+1)

        for k in range(2, K+1):
            # Now, we will develop dp2[i] = dp(k, i)
            dp2 = [0]
            x = 1
            for n in range(1, N+1):
                # Let's find dp2[n] = dp(k, n)
                # Increase our optimal x while we can make our answer better.
                # Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
                # is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
                while x < n and max(dp[x-1], dp2[n-x]) > \
                                max(dp[x], dp2[n-x-1]):
                    x += 1

                # The final answer happens at this x.
                dp2.append(1 + max(dp[x-1], dp2[n-x]))

            dp = dp2
        return dp[-1]


# Mathematical
# Time: O(klogn)
# Space: O(1)
# 2023.07.27: no
# notes: pure math proof, skipped; binary search the drop count whose
#        reachable-floor sum first covers N.
class Solution5:
    def superEggDrop(self, K: int, N: int) -> int:
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        def f(x):
            ans = 0
            r = 1
            for i in range(1, K+1):
                r *= x-i+1
                r //= i
                ans += r
                if ans >= N: break
            return ans

        lo, hi = 1, N
        while lo < hi:
            mi = (lo + hi) // 2
            if f(mi) < N:
                lo = mi + 1
            else:
                hi = mi
        return lo


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4(), Solution5()):
    assert sol.superEggDrop(1, 2) == 2
    assert sol.superEggDrop(2, 6) == 3
    assert sol.superEggDrop(3, 14) == 4
