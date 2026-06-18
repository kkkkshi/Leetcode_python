# 110. Balanced Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# depth-first Search Approach bottom up(best approach)
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
# notes: post-order recursion returning (is_balanced, height); a
#        subtree is balanced only if both children are and differ <=1
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def recursion(root):
            if root == None:
                return (True, 0)
            left_status, left_height = recursion(root.left)
            right_status, right_height = recursion(root.right)
            cur_height = max(left_height, right_height)+1
            if abs(left_height - right_height) <= 1:
                return (left_status and right_status, cur_height)
            else:
                return (False, cur_height)
        if root == None:
            return True
        final_status, final_height = recursion(root)
        return final_status


# Tests:
balanced = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
skewed = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), None), None), None)
for sol in (Solution(),):
    assert sol.isBalanced(balanced) is True
    assert sol.isBalanced(skewed) is False
    assert sol.isBalanced(None) is True
    assert sol.isBalanced(TreeNode(1)) is True
