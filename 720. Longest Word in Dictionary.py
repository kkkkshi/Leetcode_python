# 720. Longest Word in Dictionary

# Trie + Depth-First Search [Accepted]
# Time: O(sigma wi)
# Space: O(sigma wi)
# 2023.08.28: no
# notes: two steps, first insert all words, then traverse to check.
#        the insert is clever and skips checking node by node; sorting
#        by length also works but the trie fits the problem better
import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False
        self.word = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isEnd = True
        node.word = word

    def bfs(self):
        q = collections.deque([self.root])
        res = ""
        while q:
            cur = q.popleft()
            for n in cur.children.values():
                if n.isEnd:
                    q.append(n)
                    if len(n.word) > len(res) or n.word < res:
                        res = n.word
        return res


class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = Trie()
        for w in words:
            trie.insert(w)
        return trie.bfs()


# Tests:
for sol in (Solution(),):
    assert sol.longestWord(["w","wo","wor","worl","world"]) == "world"
    assert sol.longestWord(["a","banana","app","appl","ap","apply","apple"]) == "apple"
    assert sol.longestWord(["a","b","c"]) == "a"
