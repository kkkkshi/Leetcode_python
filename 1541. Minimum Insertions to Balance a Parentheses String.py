# 1541. Minimum Insertions to Balance a Parentheses String

# Greedy
# Time: O(n)
# Space: O(1)
# 2023.09.29: no
# notes: one pass tracking right-parens still needed; the tricky
#        case is when only one ')' was supplied where two are due.
#        On '(' need += 2; if need is odd, the previous step had a
#        lone ')', so add one '(' (res += 1) and need -= 1.
#        On ')' need -= 1; if need goes -1 there was no matching
#        '(', so add one '(' (res += 1) and need becomes 1.
class Solution:
    def minInsertions(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        res, need = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                need += 2
                if need % 2 == 1:
                    res += 1 # one ')' needs two; only one here, add a '('
                    need -= 1
            elif s[i] == ')':
                need -= 1
                if need == -1:
                    res += 1
                    need = 1
        return res + need


# Tests:
for sol in (Solution(),):
    assert sol.minInsertions("()(") == 3
    assert sol.minInsertions("(()))") == 1
    assert sol.minInsertions("())") == 0
    assert sol.minInsertions("))())(") == 3
