# 91. Decode Ways

# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.31: yes
# notes: recursion; if current char is '0' return 0 since '0' can't
#        start a code; if the two-digit number <= 26 recurse at
#        index+2 as well, else just recurse at index+1
from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def recursiveWithMemo(self, index, s) -> int:
        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0

        if index == len(s) - 1:
            return 1

        answer = self.recursiveWithMemo(index + 1, s)
        if int(s[index: index + 2]) <= 26:
            answer += self.recursiveWithMemo(index + 2, s)

        return answer

    def numDecodings(self, s: str) -> int:
        return self.recursiveWithMemo(0, s)


# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.31: yes
# notes: the key is to judge i-1 and i-2 in two separate cases instead
#        of adding them directly: if i-1 is valid add dp[i-1], if i-2
#        is valid add dp[i-2]; adding 1 or 2 outright would be wrong
class Solution2:
    def numDecodings(self, s: str) -> int:
        # Array to store the subproblem results
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):
            # Check if successful single digit decode is possible.
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i - 2: i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]


# Dynamic Programming
# Time: O(n)
# Space: O(1)
# 2023.07.31: yes
# notes: space-compressed version of the dp above
class Solution3:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current = one_back
            two_digit = int(s[i - 1: i + 1])
            if two_digit >= 10 and two_digit <= 26:
                current += two_back
            two_back = one_back
            one_back = current

        return one_back


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.numDecodings("226") == 3
    assert sol.numDecodings("12") == 2
    assert sol.numDecodings("127") == 2
    assert sol.numDecodings("10") == 1
    assert sol.numDecodings("2101") == 1
    assert sol.numDecodings("06") == 0
    assert sol.numDecodings("1") == 1
