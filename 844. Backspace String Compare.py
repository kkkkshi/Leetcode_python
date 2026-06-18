# 844. Backspace String Compare

import itertools


# Two Pointer approach
# Time: O(n)
# Space: O(1)
# 2023.06.08: yes
# notes: rewrite each string in place with a write pointer, backing it
#        up on '#', then compare the two trimmed prefixes
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def final_str(s):
            sp, fp = 0, 0
            for fp in range(0, len(s)):
                if s[fp] == "#":
                    if sp != 0:
                        sp -= 1
                else:
                    s[sp] = s[fp]
                    sp += 1
            return sp
        s = list(s)
        t = list(t)
        ls = final_str(s)
        lt = final_str(t)
        return s[:ls] == t[:lt]


# Two Pointer approach
# Time: O(n)
# Space: O(1)
# 2023.06.08: no
# notes: scan each string from the right; on '#' skip the next char, so
#        there's no need to check whether the write pointer is 0
class Solution2:
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))


# Build String approach
# Time: O(m+n)
# Space: O(m+n)
# 2023.06.08: no
# notes: rebuild each string with a stack, popping on '#', then compare
class Solution3:
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.backspaceCompare("ab#c", "ad#c") is True
    assert sol.backspaceCompare("ab##", "c#d#") is True
    assert sol.backspaceCompare("a#c", "b") is False
    assert sol.backspaceCompare("", "") is True
