# 211. Design Add and Search Words Data Structure

# Trie
# Time: O(n)
# Space: O(n)
# 2023.07.16: yes
# notes: store words in a trie; on search, when we hit '.' recurse
#        into every child, otherwise follow the matching child
class TrieNode:
    def __init__(self):
        self.val = False
        self.children = {}


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.val = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        self.result = False
        def recursion(node, word):
            if not word:
                if node.val:
                    self.result = True
                return
            if word[0] == ".":
                for n in node.children.values():
                    recursion(n, word[1:])
            else:
                node = node.children.get(word[0])
                if not node:
                    return
                recursion(node, word[1:])
        recursion(node, word)
        return self.result


# Tests:
test = WordDictionary()
test.addWord("bad")
test.addWord("dad")
test.addWord("mad")
test.addWord("pad")
test.addWord("bad")
assert test.search("pad") is True
assert test.search("bad") is True
assert test.search("ba") is False
assert test.search(".ad") is True
assert test.search("b..") is True
assert test.search("b.x") is False
