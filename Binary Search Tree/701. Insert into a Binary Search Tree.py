# 701. Insert into a Binary Search Tree

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(values):
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    q = deque([root])
    for val in it:
        node = q[0]
        if node.left is None:
            if val is not None:
                node.left = TreeNode(val)
                q.append(node.left)
        else:
            if val is not None:
                node.right = TreeNode(val)
                q.append(node.right)
            q.popleft()
    return root


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


# Recursion Approach
# Time: O(logn)
# Space: O(h)
# 2023.06.30: yes
# notes: recurse down to the empty spot and hang a new leaf there
class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root


# Iteration Approach
# Time: O(logn)
# Space: O(1)
# 2023.06.30: yes
# notes: same descent with a loop, attaching the leaf when a child
#        slot is empty
class Solution2:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        node = root
        while node:
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
        return TreeNode(val)


# Tests:
for sol in (Solution(), Solution2()):
    tree = build([4, 2, 7, 1, 3])
    assert inorder(sol.insertIntoBST(tree, 5)) == [1, 2, 3, 4, 5, 7]
    assert inorder(sol.insertIntoBST(None, 8)) == [8]
