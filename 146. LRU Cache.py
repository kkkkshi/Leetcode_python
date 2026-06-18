# 146. LRU Cache

import collections


# Doubly Linked List
# Time: O(1) for get and put
# Space: O(capacity)
# 2023.06.17: yes
# notes: a doubly linked list plus a hash map give O(1) get and put;
#        new nodes update both structures together
# the trick of dummy head/tail avoids messy head/tail edge cases
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DoubleList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addLast(self, x):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        self.size += 1

    def remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    def removeFirst(self):
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first

    def size(self):
        return self.size


class LRUCache:
    def makeRecently(self, key: int):
        # promote a key to most recently used
        x = self.map.get(key)
        # remove the node from the list first
        self.cache.remove(x)
        # reinsert it at the tail
        self.cache.append(x)

    def addRecently(self, key: int, val: int):
        # add a most recently used element
        x = Node(key, val)
        # the list tail is the most recently used element
        self.cache.append(x)
        # also add the key mapping in map
        self.map[key] = x

    def deleteKey(self, key: int):
        # delete a key
        x = self.map.get(key)
        # remove from the list
        self.cache.remove(x)
        # remove from the map
        self.map.pop(key)

    def removeLeastRecently(self):
        # delete the least recently used element
        # the first list element is the least recently used
        deletedNode = self.cache.pop(0)
        # also remember to remove its key from map
        deletedKey = deletedNode.key
        self.map.pop(deletedKey)

    def __init__(self, capacity: int):
        self.cache = []
        self.map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        # read
        if key not in self.map:
            return -1
        self.makeRecently(key)
        return self.map.get(key).val

    def put(self, key: int, value: int) -> None:
        # write
        if key in self.map:
            self.map.get(key).val = value
            self.makeRecently(key)
            return
        if len(self.cache) == self.capacity:
            self.removeLeastRecently()
        self.addRecently(key, value)


class LRUCache2:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = {}
        self.head = Node(-1, -1)  # dummy head for clean head/tail edges
        self.tail = Node(-1, -1)
        self.head.next = self.tail  # easy to forget
        self.tail.prev = self.head

    def add(self, node):
        # update links of the new added node
        # only adds, does not handle overflow
        previous_end = self.tail.prev
        previous_end.next = node
        node.next = self.tail
        node.prev = previous_end
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)
        node = Node(key, value)
        self.dic[key] = node    # update the hash table contents
        self.add(node)

        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]


# Built-in Approach:
# Time: O(1) for get and put
# Space: O(1)
# 2023.06.17: no
# notes: built-in OrderedDict; in interviews ask if it is allowed, the
#        doubly linked list method is the one that matters
class LRUCache3:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            self.dic.move_to_end(key)
        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(False)


# Tests:
for cls in (LRUCache, LRUCache2, LRUCache3):
    obj = cls(2)
    obj.put(1, 1)
    obj.put(2, 2)
    assert obj.get(1) == 1
    obj.put(3, 3)        # evicts key 2
    assert obj.get(2) == -1
    obj.put(4, 4)        # evicts key 1
    assert obj.get(1) == -1
    assert obj.get(3) == 3
    assert obj.get(4) == 4
