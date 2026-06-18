# 72. Edit Distance

# Memoization: Top-Down Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.24: no
# notes: looks hard but splits into 4 moves: insert, replace, delete,
#        skip. when s[i] == s[j] move both i and j back one;
#        insert moves j back, delete moves i back, replace moves both
#        back (diagonal). dp holds the steps needed up to this cell.
#        base case: when one string is done, the steps left equal the
#        other string's progress length, +1 since indexing starts at 0
class Solution:
    def __init__(self):
        self.memo = []

    def minDistance(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        # init memo with a sentinel meaning not computed yet
        self.memo = [[-1] * n for _ in range(m)]
        return self.dp(s1, m - 1, s2, n - 1)

    def dp(self, s1, i, s2, j):
        # when one word is done, just fill in the rest; +1 since i counts from 0
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1

        # check memo to avoid overlapping sub-problems
        if self.memo[i][j] != -1:
            return self.memo[i][j]

        # transition, store the result in memo
        if s1[i] == s2[j]:
            self.memo[i][j] = self.dp(s1, i - 1, s2, j - 1)
        else:
            self.memo[i][j] = min(
                self.dp(s1, i, s2, j - 1) + 1,
                self.dp(s1, i - 1, s2, j) + 1,
                self.dp(s1, i - 1, s2, j - 1) + 1
            )

        return self.memo[i][j]


# Memoization: Top-Down Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.24: no
# notes: same idea as above, the key is the base case dp[i][0] = i,
#        the steps left when one string is finished
class Solution2:
    def minDistance(self,s1: str, s2: str) -> int:
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        # dp[i+1][j+1] is the min edit distance of s1[0..i] and s2[0..j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # base case
        # If word1 is empty, the edit distance is equal to the length of word2.
        # If word2 is empty, the edit distance is equal to the length of word1.
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        # solve bottom-up
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j - 1] + 1
                    )
        # holds the min edit distance of the whole s1 and s2
        return dp[m][n]


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.minDistance("horse", "ros") == 3
    assert sol.minDistance("intention", "execution") == 5
    assert sol.minDistance("", "abc") == 3
    assert sol.minDistance("abc", "abc") == 0
