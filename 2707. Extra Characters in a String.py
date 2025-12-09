# Top Down Dynamic Programming with Substring Method
# Time: O(n^3)
# Space: O(n+m*k)
# 2023.09.02: no
# notes: dp returns the minimum number of extra characters needed to form a valid concatenation of words starting from the start index
# 有点像分解coin change，当前的方法数是当前的后后续的最小值
# ans = dp(start +1) +1代表着到达前一个节点，必然会多一个没有用到的，看看后面有没有符合的即可
# 至于为什么要+1， +1，因为str的特性，s[i:i] = ""， s[i:i+1]才有第一个字符
from functools import cache
from typing import List


class Solution(object):
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
# notes: 注意初始化的时候要n+1，因为有一个情况是最后一个字符是空的
class Solution2:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
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
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution3:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
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
class Solution4:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
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
test = Solution4()
test.minExtraChar(s = "leetscode", dictionary = ["leet","code","leetcode"])















