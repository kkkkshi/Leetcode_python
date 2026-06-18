# 392. Is Subsequence

# Two-Pointers
# Time: O(T)
# Space: O(1)
# 2023.10.01: yes
# notes: walk through t; each time t[j] matches the next s char, advance
#        i. s is a subsequence iff i reaches the end of s.
from bisect import bisect, bisect_right
from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        m = len(s)
        i = 0
        for j in range(n):
            if i == m:
                return True
            if s[i] == t[j]:
                i += 1
                j += 1
        return i == m


# Recursion (strongly discouraged)
# Time: O(T)
# Space: O(T)
# 2023.10.01: no
# notes: recurse over both indices; on match consume s, always consume t.
class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        def rec_isSubsequence(left_index, right_index):
            # base cases
            if left_index == LEFT_BOUND:
                return True
            if right_index == RIGHT_BOUND:
                return False
            # consume both strings or just the target string
            if s[left_index] == t[right_index]:
                left_index += 1
            right_index += 1

            return rec_isSubsequence(left_index, right_index)

        return rec_isSubsequence(0, 0)


# Greedy Match with Character Indices Hashmap
# Time: O(T + S*logT)
# Space: O(T)
# 2023.10.01: no
# notes: see 792; index each char of t, then binary-search the next
#        position greater than the current match for each char of s.
class Solution3:
    def isSubsequence(self, s: str, t: str) -> bool:

        letter_indices_table = defaultdict(list)
        for index, letter in enumerate(t):
            letter_indices_table[letter].append(index)

        curr_match_index = -1
        for letter in s:
            if letter not in letter_indices_table:
                return False  # no match at all, early exit

            # greedy match with binary search
            indices_list = letter_indices_table[letter]
            match_index = bisect_right(indices_list, curr_match_index)
            if match_index != len(indices_list):
                curr_match_index = indices_list[match_index]
            else:
                return False # no suitable match found, early exit

        return True


# Dynamic Programming
# Time: O(T)
# Space: O(T)
# 2023.10.01: no
# notes: dp is fine but overkill here; it is Levenshtein distance.
class Solution4:
    def isSubsequence(self, s: str, t: str) -> bool:
        source_len, target_len = len(s), len(t)

        # the source string is empty
        if source_len == 0:
            return True

        # matrix to store the history of matches/deletions
        dp = [ [0] * (target_len + 1) for _ in range(source_len + 1)]

        # DP compute, we fill the matrix column by column, bottom up
        for col in range(1, target_len + 1):
            for row in range(1, source_len + 1):
                if s[row - 1] == t[col - 1]:
                    # find another match
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    # retrieve the maximal result from previous prefixes
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

            # check if we can consume the entire source string,
            #   with the current prefix of the target string.
            if dp[source_len][col] == source_len:
                return True

        return False


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.isSubsequence("abbc", "ahbgdbc") is True
    assert sol.isSubsequence("axc", "ahbgdc") is False
    assert sol.isSubsequence("b", "abc") is True
    assert sol.isSubsequence("", "ahbgdc") is True
    assert sol.isSubsequence("abc", "") is False
