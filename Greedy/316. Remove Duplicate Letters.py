# 316. Remove Duplicate Letters

# Greedy - Solving with Stack (best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.22: no
# notes: 1. keep order with a stack, each char appears once (track via
#        inStack). 2. use a count so a stack top is only popped when it
#        still appears again later
class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []  # Stack to store the result after removing duplicates

        # keep a counter of how many of each char remain in the string
        # input is ASCII, so size 256 is enough
        count = [0] * 256
        for c in s:
            count[ord(c)] += 1

        inStack = [False] * 256
        for c in s:
            # decrement the count for each char as we pass it
            count[ord(c)] -= 1

            if inStack[ord(c)]:
                continue

            while stk and stk[-1] > c:
                # stop popping if the stack top no longer appears later
                if count[ord(stk[-1])] == 0:
                    break
                # otherwise it still appears, so we can pop it
                inStack[ord(stk.pop())] = False

            stk.append(c)
            inStack[ord(c)] = True

        sb = []
        while stk:
            sb.append(stk.pop())

        # stack pops in reverse insertion order, so reverse it back
        return ''.join(sb[::-1])


# Greedy - Solving Letter by Letter
# Time: O(n)
# Space: O(n)
# 2023.06.22: no
# notes: tricky, recursion + greedy, didn't fully get it
from collections import Counter


class Solution2:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        # find pos - the index of the leftmost letter in our solution
        # we create a counter and end the iteration once the suffix doesn't have each unique character
        # pos will be the index of the smallest character we encounter before the iteration ends
        c = Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            c[s[i]] -=1
            if c[s[i]] == 0:
                break
        # our answer is the leftmost letter plus the recursive call on the remainder of the string
        # note we have to get rid of further occurrences of s[pos] to ensure that there are no duplicates
        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], "")) if s else ''


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.removeDuplicateLetters("bcabc") == "abc"
    assert sol.removeDuplicateLetters("cbacdcbc") == "acdb"
    assert sol.removeDuplicateLetters("") == ""
    assert sol.removeDuplicateLetters("a") == "a"
