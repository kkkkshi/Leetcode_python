# 104. Maximum Depth of Binary Tree

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(values):
    # level-order list -> tree, None marks a missing node
    if not values:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


# Recursion Approach
# Time: O(n)
# Space: O(logn)
# 2023.06.26: yes
# notes: depth of a node is 1 plus the max depth of its two subtrees
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth)+1


# Iteration Approach:
# Time: O(n)
# Space: O(logn)
# 2023.06.26: yes
# notes: dfs with a stack carrying each node's depth, tracking the max
class Solution2:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        if root:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.maxDepth(build([3, 9, 20, None, None, 15, 7])) == 3
    assert sol.maxDepth(build([1, 2, None, 3, None, 4])) == 4
    assert sol.maxDepth(build([1])) == 1
    assert sol.maxDepth(build([])) == 0
