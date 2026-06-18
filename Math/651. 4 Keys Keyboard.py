# 651. 4 Keys Keyboard

# Dynamic Programming Approach
# Time: O(n)
# Space: O(n)
# 2023.07.28: no
# notes: dp[j] is the most A's using j presses. found that for an
#        earlier i in [0,3), dp[j] = (j-i-1) * dp[i] for i+3 <= j <=
#        i+6; past i+6 you would redo select-copy-paste, so j only
#        needs to scan i+3 to i+6
class Solution:
    def maxA(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = list(range(n + 1))
        for i in range(n - 2):
            for j in range(i + 3, min(n, i + 6) + 1):
                dp[j] = max(dp[j], (j - i - 1) * dp[i])
        return dp[n]


# Dynamic Programming Approach
# Time: O(n)
# Space: O(n)
# 2023.07.28: no
# notes: brute-force dp with no shortcuts. dp[j-2] is the A count at
#        copy time, and i-j+1 counts the paste repeats, not the
#        current total
class Solution2:
    def maxA(self,N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0] * (N + 1)
        dp[0] = 0
        for i in range(1, N+1):
            # press A
            dp[i] = dp[i - 1] + 1
            for j in range(2, i):
                # select-all and copy dp[j-2], then paste i - j times
                # the screen then has dp[j - 2] * (i - j + 1) A's
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
        # how many A's at most after N presses?
        return dp[N]


# Dynamic Programming Approach
# Time: O(n)
# Space: O(n)
# 2023.07.28: no
# notes: clever, still leans on some math: the best can only come from
#        pasting the copy two, three, or four times; beyond that you
#        could just double instead
class Solution3:
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        f = list(range(N+1))
        for i in range(7, N+1):
            f[i] = max(f[i-3]*2, f[i-4]*3, f[i-5]*4)

        return f[N]


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.maxA(1) == 1
    assert sol.maxA(3) == 3
    assert sol.maxA(7) == 9
    assert sol.maxA(10) == 20
