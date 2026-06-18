# 139. Word Break

from typing import List
from collections import deque
from functools import cache


# Breadth-First Search
# Time: O(n^3 + mk)
# Space: O(n+m*k)
# 2023.07.22: yes
# notes: start a BFS from index 0; for each reachable start, push every
#        end whose substring is a word, mark seen so we don't repeat
class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        queue = deque([0])
        seen = set()

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue

                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)
        return False


# Top-Down Dynamic Programming
# Time: O(nmk)
# Space: O(n)
# 2023.07.22: no
# notes: recurse from i = len(s)-1; match a word ending at i and recurse
#        on i - len(word), so the prefix shrinks one word at a time
class Solution2:
    def wordBreak(self, s, wordDict):
        @cache
        def dp(i):
            if i < 0:
                return True
            for word in wordDict:
                if s[i - len(word) + 1:i + 1] == word and dp(i - len(word)):
                    return True
            return False
        return dp(len(s) - 1)


# Bottom-Up Dynamic Programming
# Time: O(nmk)
# Space: O(n)
# 2023.07.22: no
# notes: dp[i] means s[:i+1] is breakable; mark True if a word covers
#        s up to i, or follows a True ending at i - len(word)
# same as the cached method but stores results in an array
class Solution3:
    def wordBreak(self, s, wordDict):
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                # Handle out of bounds case
                if i < len(word) - 1:
                    continue
                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1:i + 1] == word:
                        dp[i] = True
                        break
        return dp[-1]


# Trie Optimization
# Time: O(n^2+mk)
# Space: O(n+mk)
# 2023.07.22: no
# notes: build a trie of words; from each True position walk the trie
#        and mark every end that completes a word, like the dp above
#        but the word-matching step is sped up
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Solution4:
    def wordBreak(self, s, wordDict):
        root = TrieNode()
        for word in wordDict:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_word = True
        dp = [False] * len(s)
        for i in range(len(s)):
            if i == 0 or dp[i - 1]:
                curr = root
                for j in range(i, len(s)):
                    c = s[j]
                    if c not in curr.children:
                        # No words exist
                        break
                    curr = curr.children[c]
                    if curr.is_word:
                        dp[j] = True
        return dp[-1]


# Backtracking (time exceed)
# notes: only here to contrast backtracking with dp; times out
class Solution5:
    def __init__(self):
        self.wordDict = []
        # whether a valid answer was found
        self.found = False
        # the backtracking path
        self.track = []

    # main entry
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.found = False
        self.track = []
        self.wordDict = wordDict
        # run backtracking over all possible combinations
        self.backtrack(s, 0)
        return self.found

    # backtracking template
    def backtrack(self, s: str, i: int):
        # base case
        if self.found:
            # stop searching once an answer is found
            return
        if i == len(s):
            # whole s matched, one valid answer found
            self.found = True
            return

        # backtracking template
        for word in self.wordDict:
            # see which word matches the prefix of s[i..]
            length = len(word)
            if i + length <= len(s) and s[i:i+length] == word:
                # found a word matching s[i..i+length)
                # make the choice
                self.track.append(word)
                # go to the next level, keep matching s[i+length..]
                self.backtrack(s, i+length)
                # undo the choice
                self.track.pop()


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4(), Solution5()):
    assert sol.wordBreak("leetcode", ["leet", "code"]) is True
    assert sol.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert sol.wordBreak("catsandog",
                         ["cats", "dog", "sand", "and", "cat"]) is False
