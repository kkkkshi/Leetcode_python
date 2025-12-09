# Linked Lists
# Time: O(1)
# Space: O(1)
# 2023.09.05: yes
# notes: 注意一下None就行，新节点的后续有可能是none, random也有可能指none，所以random.next不一定可以
# Definition for a Node.
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
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

#  Iterative with O(N) Space
# Time: O(n)
# Space: O(n)
# 2023.09.05: yes
# notes: 最简单的一种，用hashmap对应
class Solution2(object):
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
# notes: 递归方法，遇到一个新node就新建一个node，然后用hashmap对应关系即可，递归调用node.next和node.random
class Solution3(object):
    """
    :type head: Node
    :rtype: Node
    """
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head):

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
c = Node(3)
d = Node(3)
e = Node(3)
c.next = d
d.next = e
d.random = c
test = Solution3()
t = test.copyRandomList(c)
a = Node(1)
b = Node(2)
a.next = b
a.random = b
b.random = b
test.copyRandomList(a)


