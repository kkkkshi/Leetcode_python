# 140. Word Break II

from collections import defaultdict, Counter


# Top-Down Dynamic Programming
# Time: O(n^2+2^n+w)
# Space: O(2^n*n+w)
# 2023.07.24: no
# notes: still backtracking, but memo maps each suffix to all word
#        lists that build it, then we join them into sentences
class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        # table to map a string to its corresponding words break
        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        memo = defaultdict(list)
        def _wordBreak_topdown(s):
            """ return list of word lists """
            if not s:
                return [[]]  # list of empty list

            if s in memo:
                # returned the cached solution directly.
                return memo[s]

            for endIndex in range(1, len(s)+1):
                word = s[:endIndex]
                if word in wordSet:
                    # move forwards to break the postfix into words
                    for subsentence in _wordBreak_topdown(s[endIndex:]):
                        memo[s].append([word] + subsentence)
            return memo[s]

        # break the input string into lists of words list
        _wordBreak_topdown(s)

        # chain up the lists of words into sentences.
        return [" ".join(words) for words in memo[s]]


# Bottom-Up Dynamic Programming
# Time: O(n^2+2^n+w)
# Space: O(2^n*n+w)
# 2023.07.24: no
# notes: dp[i] holds every sentence formed up to index i; base dp[0]
#        is "", and each matched word appends to earlier sentences
class Solution2:
    def wordBreak(self, s, wordDict):
        # quick check on the characters,
        #   otherwise it would exceed the time limit for certain test cases.
        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
            return []
        wordSet = set(wordDict)
        dp = [[]] * (len(s)+1)
        dp[0] = [""]
        for endIndex in range(1, len(s)+1):
            sublist = []
            # fill up the values in the dp array.
            for startIndex in range(0, endIndex):
                word = s[startIndex:endIndex]
                if word in wordSet:
                    for subsentence in dp[startIndex]:
                        sublist.append((subsentence + ' ' + word).strip())
            dp[endIndex] = sublist
        return dp[len(s)]


# Backtracking
# Time: O(n^2+2^n+w)
# Space: O(2^n*n+w)
# 2023.07.24: no
# notes: plain brute-force recursion: at index i try each word that
#        matches the prefix, recurse, and record the path when i hits end
class Solution3:
    def __init__(self):
        # results
        self.res = []
        # the backtracking path
        self.track = []
        self.wordDict = []

    # main entry
    def wordBreak(self, s, wordDict):
        self.res = []
        self.track = []
        self.wordDict = wordDict
        # run backtracking over all possible combinations
        self.backtrack(s, 0)
        return self.res

    # backtracking template
    def backtrack(self, s: str, i: int) -> None:
        # base case
        if i == len(s):
            # one valid combination spells out the whole s, to string
            self.res.append(' '.join(self.track))
            return

        # backtracking template
        for word in self.wordDict:
            # see which word matches the prefix of s[i..]
            length = len(word)
            if i + length <= len(s) and s[i:i + length] == word:
                # found a word matching s[i..i+len)
                # make the choice
                self.track.append(word)
                # go to the next level, keep matching s[i+len..]
                self.backtrack(s, i + length)
                # undo the choice
                self.track.pop()


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sorted(sol.wordBreak(
        "catsanddog", ["cat", "cats", "and", "sand", "dog"])) == \
        ["cat sand dog", "cats and dog"]
    assert sorted(sol.wordBreak(
        "pineapplepenapple",
        ["apple", "pen", "applepen", "pine", "pineapple"])) == \
        ["pine apple pen apple", "pine applepen apple",
         "pineapple pen apple"]
    assert sol.wordBreak("catsandog",
                         ["cats", "dog", "sand", "and", "cat"]) == []
