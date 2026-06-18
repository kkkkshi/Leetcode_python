# 151. Reverse Words in a String

# Reverse the Whole String and Then Reverse Each Word
# Time: O(n)
# Space: O(n)
# 2023.06.19: no
# notes: hard to come up with, but easy to write once known:
#        reverse the whole list, then reverse each word back
class Solution:
    def trim_zeros(self, s):
        result = []
        for i in range(len(s)-1):
            if (s[i] == ' ' and s[i+1] != ' ') or (s[i] != ' '):
                result.append(s[i])
        result.append(s[len(s)-1])
        if result[0] == ' ':
            result.pop(0)
        if result[-1] == ' ':
            result.pop(-1)
        return result

    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        return s

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = self.trim_zeros(s)
        s = self.reverse(s,0,len(s)-1)
        start = end = 0
        while start < len(s):
            while end < len(s) and s[end] != ' ':
                end += 1
            self.reverse(s, start, end-1)
            start = end+1
            end += 1
        return ''.join(s)


# Built-in Split + Reverse
# Time: O(n)
# Space: O(n)
# 2023.06.19: yes
# notes: split on whitespace, reverse the word list, join back
class Solution2:
    def reverseWords(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        return " ".join(reversed(s.split()))


# Deque of Words
# Time: O(n)
# Space: O(n)
# 2023.06.19: no
# notes: scan chars, build each word, push it to the front of a
#        deque so the order ends up reversed
from collections import deque
class Solution3:
    def reverseWords(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1

        d, word = deque(), []
        # push word by word in front of deque
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))

        return ' '.join(d)


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.reverseWords("the sky is blue") == "blue is sky the"
    assert sol.reverseWords("  hello world  ") == "world hello"
    assert sol.reverseWords("a good   example") == "example good a"
