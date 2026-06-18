# 5. Longest Palindromic Substring

# Expand From Centers Approach (best approach):
# Time: O(n^2)
# Space: O(1)
# 2023.06.18: no
# notes: for each center s[i] (odd) or s[i], s[j] (even) find the
# longest palindrome around it and keep the longest seen
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            s1 = self.parlindrome(s, i, i)
            s2 = self.parlindrome(s, i, i+1)
            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return res

    def parlindrome(self, s, l, r):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        return s[l+1:r]


# Check All Substrings
# Time: O(n^3)
# Space: O(1)
# 2023.06.18: yes
# notes: try substrings longest first; return the first palindrome
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        def check(i, j):
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start:start + length]

        return ""


# Dynamic Programming Approach
# Time: O(n^2)
# Space: O(n^2)
# 2023.06.18: no
# notes: 08.15 update:
# dp[i][j] is True if s[i..j] is a palindrome
# two base cases: single char i-i; adjacent pair i-(i+1)
# everything else builds out from those two
class Solution3:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i:j + 1]


# Manacher's Algorithm
# notes: R is the farthest right reach, C the center
# 1. i is outside R -> expand by brute force
# 2a. i's mirror palindrome stays inside R, same as i' (i's
#     mirror about C)
# 2b. i's mirror reaches outside R, so R-i is the length, else C
#     can expand further
# 2c. i's palindrome lands exactly on the R, L bound, unknown
#     beyond L -> expand by brute force
class Solution4:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        s_prime = '#' + '#'.join(s) + '#'
        n = len(s_prime)
        palindrome_radii = [0] * n
        center = radius = 0
        for i in range(n):
            mirror = 2 * center - i
            if i < radius:
                palindrome_radii[i] = min(radius - i, palindrome_radii[mirror])
            while (i + 1 + palindrome_radii[i] < n and
                   i - 1 - palindrome_radii[i] >= 0 and
                   s_prime[i + 1 + palindrome_radii[i]] == s_prime[i - 1 - palindrome_radii[i]]):
                palindrome_radii[i] += 1
            if i + palindrome_radii[i] > radius:
                center = i
                radius = i + palindrome_radii[i]
        max_length = max(palindrome_radii)
        center_index = palindrome_radii.index(max_length)
        start_index = (center_index - max_length) // 2
        longest_palindrome = s[start_index: start_index + max_length]
        return longest_palindrome


# Tests:
# "babad" has two valid answers (bab/aba), so check it is a
# palindrome of the right length; the others are unique.
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    r = sol.longestPalindrome("babad")
    assert r == r[::-1] and len(r) == 3
    assert sol.longestPalindrome("cbbd") == "bb"
    assert sol.longestPalindrome("a") == "a"
    assert sol.longestPalindrome("ac") in ("a", "c")
