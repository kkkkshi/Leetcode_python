# 409. Longest Palindrome

# Greedy Approach
# Time: O(n)
# Space: O(1)
# 2023.06.25: yes
# notes: take all even counts in full and the even part of odd counts;
#        if any odd count exists, one extra char can sit in the middle.
from collections import Counter


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = Counter(s)
        total = 0
        odd = False
        for value in counts.values():
            if value % 2 == 0:
                total += value
            else:
                odd = True
                total += ((value//2)*2)
        if odd:
            total += 1
        return total


# Greedy Approach
# Time: O(n)
# Space: O(1)
# 2023.6.25: yes
# notes: same as above, just shorter; mine was a bit long.
class Solution2:
    def longestPalindrome(self, s):
        ans = 0
        for v in Counter(s).values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.longestPalindrome('abccccdd') == 7
    assert sol.longestPalindrome('ccc') == 3
    assert sol.longestPalindrome('a') == 1
    assert sol.longestPalindrome('bb') == 2
