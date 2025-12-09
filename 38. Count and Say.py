# Straightforward Approach
# Time: O(4^(n/3))
# Space: O(4^(n/3))
# 2023.07.22: no
class Solution1:
    def countAndSay(self, n):
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

class Solution2(object):
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            # m.group(0) is the entire match, m.group(1) is its first digit
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s

# Tests:
# test = Solution()
# test.countAndSay(5)


class Solution(object):
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
test = Solution()
test.countAndSay(6)

# 111221
# "312211"


