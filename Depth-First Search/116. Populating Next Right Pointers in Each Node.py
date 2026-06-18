# 116. Populating Next Right Pointers in Each Node

import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None


# Level Order Traversal Approach
# Time: O(n)
# Space: O(n)
# 2023.06.26: yes
# notes: BFS level by level; for a perfect tree, count nodes and
#        cut next at the end of each row using 2**j - 1
class Solution:
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        saving = [root]
        i, j = 0, 1   # j power, i num of nodes
        while saving:
            cur = saving.pop(0)
            i += 1
            if i == 2 ** j -1:
                j += 1
                cur.next = None
            else:
                cur.next = saving[0]
            if cur.left:
                saving.append(cur.left)
            if cur.right:
                saving.append(cur.right)
        return root


# Level Order Traversal Approach
# Time: O(n)
# Space: O(n)
# 2023.06.26: yes
# notes: same idea, but plain BFS without the perfect-tree
#        assumption, so it handles more general cases
class Solution2:
    def connect(self, root):
        if not root:
            return root

        Q = collections.deque([root])
        while Q:
            size = len(Q)
            for i in range(size):
                node = Q.popleft()
                if i < size - 1:
                    node.next = Q[0]
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return root


# Using previously established next pointers Approach(best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.26: no
# notes: reuse the next links just built one level up; two link
#        types: left-to-right child, and right child to the next
#        node's left child, still a BFS
class Solution3:
    def connect(self, root):
        if not root:
            return root

        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root

        # Once we reach the final level, we are done
        while leftmost.left:

            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the
            # corresponding links for the next level
            head = leftmost
            while head:

                # CONNECTION 1
                head.left.next = head.right

                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left

                # Progress along the list (nodes on the current level)
                head = head.next

            # Move onto the next level
            leftmost = leftmost.left

        return root


def build():
    return TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
                    TreeNode(3, TreeNode(6), TreeNode(7)))


def next_rows(root):
    # collect node values level by level following next pointers
    rows = []
    leftmost = root
    while leftmost:
        row = []
        node = leftmost
        while node:
            row.append(node.val)
            node = node.next
        rows.append(row)
        leftmost = leftmost.left
    return rows


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert next_rows(sol.connect(build())) == [[1], [2, 3], [4, 5, 6, 7]]
    assert sol.connect(None) is None
