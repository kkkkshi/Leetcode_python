# 38. Count and Say

# Straightforward Approach
# Time: O(4^(n/3))
# Space: O(4^(n/3))
# 2023.07.22: no
# notes: build each term by counting runs of equal digits
class Solution1:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        current_string = '1'
        for _ in range(n - 1):
            next_string = ''
            j = 0
            k = 0
            while j < len(current_string):
                while (k < len(current_string) and
                        current_string[k] == current_string[j]):
                    k += 1
                next_string += str(k - j) + current_string[j]
                j = k
            current_string = next_string
        return current_string


# Regular Expression Approach
# Time: O(4^(n/3))
# Space: O(4^(n/3))
# 2023.07.22: no
# notes:(.) match for anything, \\ match for what previous ones is
import re


class Solution2:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            # m.group(0) is the entire match, m.group(1) is its first digit
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s


# Recursive Approach
# Time: O(4^(n/3))
# Space: O(4^(n/3))
# 2023.07.22: no
# notes: recurse to get term n-1, then run-length encode it
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def check(s):
            res = ""
            c = s[0]
            cur_num = 1
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    cur_num += 1
                else:
                    res += str(cur_num) + c
                    c = s[i]
                    cur_num = 1
            res += str(cur_num) + c
            return res

        def cal(n, s):
            if n == 1:
                return check(s)
            else:
                return check(cal(n-1, s))
        if n == 1:
            return "1"
        return cal(n-1, "1")


# Tests:
for sol in (Solution1(), Solution2(), Solution()):
    assert sol.countAndSay(1) == "1"
    assert sol.countAndSay(4) == "1211"
    assert sol.countAndSay(5) == "111221"
    assert sol.countAndSay(6) == "312211"
