# 647. Palindromic Substrings

# Dynamic Programming Approach
# Time: O(n^3)
# Space: O(n)
# 2023.07.22: yes
# notes: for each end i, check every start j by expanding inward to
#        test if s[j..i] is a palindrome; slow but works
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [0] * (length + 1)
        for i in range(length):
            for j in range(0, i + 1):
                left, right = j, i
                while left < right:
                    if s[left] != s[right]:
                        break
                    else:
                        left += 1
                        right -= 1
                if left >= right:
                    dp[i + 1] += 1
            dp[i + 1] += dp[i]
        return dp[length]


# Dynamic Programming Approach
# Time: O(n^2)
# Space: O(n^2)
# 2023.07.22: no
# notes: better dp; base cases are length 1 and 2, then a substring is
#        a palindrome if its inner part is and the ends match
class Solution2:
    def countSubstrings(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0

        if n <= 0:
            return 0

        dp = [[False for _ in range(n)] for _ in range(n)]

        # Base case: single letter substrings
        for i in range(n):
            dp[i][i] = True
            ans += 1

        # Base case: double letter substrings
        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            ans += 1 if dp[i][i + 1] else 0

        # All other cases: substrings of length 3 to n
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                ans += 1 if dp[i][j] else 0
        return ans


# Expand Around Possible Centers
# Time: O(n^2)
# Space: O(1)
# 2023.07.22: no
# notes: simplest one; take each index (and each adjacent pair) as a
#        center and expand outward while the two ends match
class Solution3:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)):
            # odd-length palindromes, single character center
            ans += self.countPalindromesAroundCenter(s, i, i)
            # even-length palindromes, consecutive characters center
            ans += self.countPalindromesAroundCenter(s, i, i + 1)
        return ans

    def countPalindromesAroundCenter(self, ss, lo, hi):
        ans = 0
        while lo >= 0 and hi < len(ss):
            if ss[lo] != ss[hi]:
                break  # the first and last characters don't match!
            # expand around the center
            lo -= 1
            hi += 1
            ans += 1
        return ans


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.countSubstrings("abc") == 3
    assert sol.countSubstrings("aaa") == 6
    assert sol.countSubstrings("abcdcb") == 8
    assert sol.countSubstrings("a") == 1
