# 516. Longest Palindromic Subsequence

# Recursive Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: no
# notes: lps(l, r) is the answer on s[l..r]; if ends match add 2 and
#        shrink both, else drop one side and take the better
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = {}
        def lps(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                memo[(l, r)] = lps(l + 1, r - 1) + 2
            else:
                memo[(l, r)] = max(lps(l, r - 1), lps(l + 1, r))
            return memo[(l, r)]

        return lps(0, n - 1)


# Iterative Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: yes
# notes: the transition is the key part; dp[i][j] is the longest
#        palindrome on s[i..j], and the j < i part is left as 0
class Solution2:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n-1]


# Dynamic Programming with Space Optimization
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: no
# notes: same recurrence as Solution2 but keep only the previous row
class Solution3:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp, dpPrev = [0 for _ in range(n)],[0 for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[j] = dpPrev[j-1]+2
                else:
                    dp[j] = max(dpPrev[j], dp[j-1])
            dpPrev = dp[:]
        return dp[n-1]


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.longestPalindromeSubseq("bbbab") == 4
    assert sol.longestPalindromeSubseq("cbbd") == 2
    assert sol.longestPalindromeSubseq("a") == 1
    assert sol.longestPalindromeSubseq("abcde") == 1
