# 138. Copy List with Random Pointer

# Definition for a Node.
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def build(data):
    # data is a list of [val, random_index]; random_index is None or
    # the index of the node pointed to by random
    if not data:
        return None
    nodes = [Node(val) for val, _ in data]
    for i in range(len(nodes)):
        nodes[i].next = nodes[i + 1] if i + 1 < len(nodes) else None
        rand = data[i][1]
        nodes[i].random = nodes[rand] if rand is not None else None
    return nodes[0]


def serialize(head):
    # turn a random-pointer list back into [val, random_index] form
    order = []
    index = {}
    cur = head
    while cur:
        index[cur] = len(order)
        order.append(cur)
        cur = cur.next
    out = []
    for node in order:
        rand = index[node.random] if node.random is not None else None
        out.append([node.val, rand])
    return out


# Linked Lists
# Time: O(1)
# Space: O(1)
# 2023.09.05: yes
# notes: watch out for None; a new node's next may be none and random
# may point to none, so random.next is not always usable.
# interleave each clone after its original, then unweave.
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = Node(cur.val, tmp, None)
            cur = tmp
        cur = head
        while cur:
            tmp = cur.next.next
            if tmp == None:
                cur.next.next = None
            else:
                cur.next.next = tmp.next
            if cur.random == None:
                cur.next.random = None
            else:
                cur.next.random = cur.random.next
            cur = tmp
        return head.next


# Iterative with O(N) Space
# Time: O(n)
# Space: O(n)
# 2023.09.05: yes
# notes: simplest one, map old node -> new node in a hashmap
class Solution2:
    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
        self.visited = {}

    def getClonedNode(self, node):
        # If node exists then
        if node:
            # Check if its in the visited dictionary
            if node in self.visited:
                # If its in the visited dictionary then return the new node reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise create a new node, save the reference in the visited dictionary and return it.
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return head

        old_node = head
        # Creating the new head node.
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node != None:

            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]


# Recursive with O(N) Space
# Time: O(n)
# Space: O(n)
# 2023.09.05: yes
# notes: recursive; on each new node make a clone and map it, then
#        recurse on node.next and node.random
class Solution3:
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None

        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this would help us avoid them.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert serialize(sol.copyRandomList(build([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]))) \
        == [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    assert serialize(sol.copyRandomList(build([[1, 1], [2, 1]]))) == [[1, 1], [2, 1]]
    assert serialize(sol.copyRandomList(build([]))) == []
    assert serialize(sol.copyRandomList(build([[3, None]]))) == [[3, None]]
