# 98. Validate Binary Search Tree

import math
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(values):
    # level-order build; None means missing node
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    queue = deque([root])
    while queue:
        node = queue.popleft()
        try:
            v = next(it)
        except StopIteration:
            break
        if v is not None:
            node.left = TreeNode(v)
            queue.append(node.left)
        try:
            v = next(it)
        except StopIteration:
            break
        if v is not None:
            node.right = TreeNode(v)
            queue.append(node.right)
    return root


# Recursive Traversal with Valid Range Algorithm (best approach)
# Time: O(n)
# Space: O(n)
# 2023.06.29: yes
# notes: pass down (min, max) bounds; each node must sit strictly
#        inside its allowed range
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def valid(root, min, max):
            if root == None:
                return True
            if root.val >= max or root.val <= min:
                return False
            left_valid = valid(root.left, min, root.val)
            right_valid = valid(root.right, root.val, max)
            return left_valid and right_valid

        return valid(root, float('-inf'), float('inf'))


# Iterative Traversal with Valid Range Algorithm (best approach)
# Time: O(n)
# Space: O(n)
# 2023.06.29: yes
# notes: same range check but with an explicit stack of (node, lo, hi)
class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True


# Recursive Inorder Traversal Algorithm (best approach)
# Time: O(n)
# Space: O(n)
# 2023.06.29: yes
# notes: inorder of a BST is strictly increasing; track the previous
#        value and fail if the order breaks
class Solution3:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)


# Iterative Inorder Traversal
# Time: O(n)
# Space: O(n)
# 2023.06.29: yes
# notes: iterative inorder with a stack; each visited value must be
#        greater than the previous one
class Solution4:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.isValidBST(None) is True
    assert sol.isValidBST(build([2, 1, 3])) is True
    assert sol.isValidBST(build([5, 1, 4, None, None, 3, 6])) is False
    assert sol.isValidBST(build([10, 5, 15, None, None, 6, 20])) is False
    assert sol.isValidBST(build([1])) is True
