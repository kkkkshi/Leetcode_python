# 1804. Implement Trie II (Prefix Tree)

# Trie
# Time: insert, search, search_prefix: O(m)
# Space: insert: O(m), search, search_prefix: O(1)
# 2023.07.16: yes
# notes: each node tracks val (word ends here) and passby (words
#        passing through), so counts and prefixes are O(m)
class TrieNode:
    def __init__(self):
        self.val = 0
        self.passby = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
                node.children[i].passby = 1
            else:
                node.children[i].passby += 1
            node = node.children[i]
        node.val += 1

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        node = self.root
        for i in word:
            if i not in node.children:
                return 0
            node = node.children[i]
        return node.val

    def countWordsStartingWith(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for i in prefix:
            if i not in node.children:
                return 0
            node = node.children[i]
        return node.passby

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for i in word:
            node = node.children[i]
            node.passby -= 1
        node.val -= 1


# Tests:
trie = Trie()
trie.insert("apple")
trie.insert("apple")
assert trie.countWordsEqualTo("apple") == 2
assert trie.countWordsStartingWith("app") == 2
trie.erase("apple")
assert trie.countWordsEqualTo("apple") == 1
assert trie.countWordsStartingWith("app") == 1
trie.erase("apple")
assert trie.countWordsStartingWith("app") == 0
assert trie.countWordsEqualTo("apple") == 0
