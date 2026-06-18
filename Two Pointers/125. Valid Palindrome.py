# 125. Valid Palindrome

# Two Pointer Algorithm (best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.24: yes
# notes: walk two pointers inward, skip non-alphanumeric chars, and
#        compare the rest case-insensitively
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


# Tests:
for sol in (Solution(),):
    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True
    assert sol.isPalindrome("race a car") is False
    assert sol.isPalindrome("") is True
    assert sol.isPalindrome(" ") is True
