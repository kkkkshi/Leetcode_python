# Two Pointer approach
# Time: O(n)
# Space: O(1)
# 2023.06.08: yes
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
# notes: reverse这个string，如果遇到#，就skip下一个，就不用验证sp是不是0了
class Solution(object):
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

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))


# Build String approach
# Time: O(m+n)
# Space: O(m+n)
# 2023.06.08: no
class Solution(object):
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

test = Solution()
test.backspaceCompare(s = "ab#c", t = "ad#c")