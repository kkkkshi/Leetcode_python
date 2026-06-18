# 677. Map Sum Pairs

# Trie
# Time: insert, sum: O(k)
# Space: insert, sum: O(k)
# 2023.07.17: yes
# notes: store each key in a trie; every node carries the summed value
#        of keys passing through it, so sum(prefix) is one lookup
import collections


class TrieNode:
    def __init__(self):
        self.val = 0
        self.passby = 0
        self.children = {}


class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        if key in self.map:
            ori_val = self.map[key]
        node = self.root
        for i in key:
            if i not in node.children:
                node.children[i] = TrieNode()
                node.children[i].passby = val
            else:
                if key in self.map:
                    node.children[i].passby += (val - ori_val)
                else:
                    node.children[i].passby += val
            node = node.children[i]
        node.val = val
        self.map[key] = val

    def sum(self, prefix):
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


# Brute Force
# Time: insert, sum: O(1)
# Space: insert, sum: O(n)
# 2023.07.17: no
# notes: works but unnecessary
class MapSum2:
    def __init__(self):
        self.map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.map[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return sum(val for key, val in self.map.items()
                   if key.startswith(prefix))


# Prefix Hashmap
# Time: insert: O(k^2), sum: O(1)
# Space: insert: O(k^2), sum: O(1)
# 2023.07.17: no
# notes: works but unnecessary
class MapSum3:
    def __init__(self):
        self.map = {}
        self.score = collections.Counter()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        for i in range(len(key) + 1):
            prefix = key[:i]
            self.score[prefix] += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.score[prefix]


# Tests:
for MapSumImpl in (MapSum, MapSum2, MapSum3):
    sol = MapSumImpl()
    sol.insert("apple", 3)
    assert sol.sum("ap") == 3
    sol.insert("app", 2)
    assert sol.sum("ap") == 5
    sol.insert("apple", 5)
    assert sol.sum("ap") == 7
    assert sol.sum("b") == 0
