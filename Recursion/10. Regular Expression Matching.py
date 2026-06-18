# 10. Regular Expression Matching

# Bottom Up Dynamic Programming
# Time: O(TP)
# Space: O(TP)
# 2023.07.27: no
# notes: aa can match a*b*c* since b* and c* can be zero. the line
#        ans = dp(i, j+2) or first_match and dp(i+1, j) covers the case
#        where the current char does not match but a * follows it.
class Solution:
    def isMatch(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: bool
        """
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)


# Top Down Dynamic Programming
# Time: O(TP)
# Space: O(TP)
# 2023.07.27: no
# notes: and binds tighter than or; otherwise the idea is the same as
#        the previous method. the dp base case is just the recursion
#        base case, so building it backwards mirrors the recursion.
class Solution2:
    def isMatch(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: bool
        """
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]


# Recursion (exceed time limit)
# Time: O((T+P)^(2^(T+P/2)))
# Space: O(T^2+P^2)
# 2023.07.27: no
# notes: each call checks if the first char matches; if it does, match
#        the rest. with a *, either skip two pattern chars or keep
#        matching the current char.
class Solution3:
    def isMatch(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: bool
        """
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.isMatch("aa", "a") == False
    assert sol.isMatch("aa", "a*") == True
    assert sol.isMatch("ab", ".*") == True
    assert sol.isMatch("aab", "c*a*b") == True
    assert sol.isMatch("mississippi", "mis*is*p*.") == False
    assert sol.isMatch("aa", "a*b*c*") == True
