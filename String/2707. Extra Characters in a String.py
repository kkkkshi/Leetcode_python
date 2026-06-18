# 2707. Extra Characters in a String

from functools import cache
from typing import List


# Top Down Dynamic Programming with Substring Method
# Time: O(n^3)
# Space: O(n+m*k)
# 2023.09.02: no
# notes: dp(start) is the min extra chars for s[start:]; either skip
#        s[start] for +1, or match a dictionary word and jump past it.
#        like coin change: each state is the best over later states.
class Solution:
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        n, dictionary = len(s), set(dictionary)
        @cache
        def dp(start):
            if start == len(s):
                return 0
            ans = dp(start + 1) + 1
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary:
                    ans = min(ans, dp(end + 1))
            return ans

        return dp(0)


# Bottom Up Dynamic Programming with Substring Method
# Time: O(n^3)
# Space: O(n+m*k)
# 2023.09.02: no
# notes: same dp built from the end; size n+1 so dp[n]=0 covers the
#        empty tail after the last character
class Solution2:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        n = len(s)
        dictionary = set(dictionary)
        dp = [0]*(n+1)
        for i in range(len(s)-1, -1, -1):
            dp[i] = dp[i+1] +1
            for j in range(i, len(s)):
                if s[i:j+1] in dictionary:
                    dp[i] = min(dp[i], dp[j+1])
        return dp[0]


# Top Down Dynamic Programming with Trie
# Time: O(n^2+MK)
# Space: O(N+MK)
# 2023.09.02: no
# notes: same top-down dp, but walk a trie from start so word matches
#        are found without slicing substrings each time
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution3:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        def buildTrie(dictionary):
            root = TrieNode()
            for word in dictionary:
                cur = root
                for c in word:
                    if c not in cur.children:
                        cur.children[c] = TrieNode()
                    cur = cur.children[c]
                cur.is_word = True
            return root

        n = len(s)
        root = buildTrie(dictionary)
        @cache
        def dp(start):
            if start == n:
                return 0
            ans = dp(start+1)+1
            cur = root
            for end in range(start, n):
                if s[end] not in cur.children:
                    break
                cur = cur.children[s[end]]
                if cur.is_word:
                    ans = min(ans, dp(end+1))
            return ans
        return dp(0)


# Bottom Up Dynamic Programming with Trie
# Time: O(n^2+MK)
# Space: O(N+MK)
# 2023.09.02: no
# notes: same bottom-up dp, walking the trie from each i to find word
#        matches instead of slicing substrings
class Solution4:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        def buildTrie(dictionary):
            root = TrieNode()
            for word in dictionary:
                cur = root
                for c in word:
                    if c not in cur.children:
                        cur.children[c] = TrieNode()
                    cur = cur.children[c]
                cur.is_word = True
            return root
        n = len(s)
        root = buildTrie(dictionary)
        dp = [0] * (n + 1)
        for i in range(len(s) - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            cur = root
            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.is_word:
                    dp[i] = min(dp[i], dp[j+1])
        return dp[0]


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.minExtraChar("leetscode", ["leet","code","leetcode"]) == 1
    assert sol.minExtraChar("sayhelloworld", ["hello","world"]) == 3
    assert sol.minExtraChar("abc", ["a","b","c"]) == 0
    assert sol.minExtraChar("xyz", ["a"]) == 3
