# 543. Diameter of Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Depth-first Search Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.26: yes
# notes: post-order; each node returns its height, and the
#        diameter is the best left+right height seen
class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diameter = 0
        def diameter(root):
            if root == None:
                return 0
            left_length = diameter(root.left)
            right_length = diameter(root.right)
            self.max_diameter  = max(self.max_diameter, left_length + right_length)
            return max(left_length, right_length) +1
        diameter(root)
        return self.max_diameter


# Tests:
a = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
b = TreeNode(1, TreeNode(2))
for sol in (Solution(),):
    assert sol.diameterOfBinaryTree(a) == 3
    assert sol.diameterOfBinaryTree(b) == 1
    assert sol.diameterOfBinaryTree(TreeNode(1)) == 0
    assert sol.diameterOfBinaryTree(None) == 0
