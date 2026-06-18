# 235. Lowest Common Ancestor of a Binary Search Tree

class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


# Recursive Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: yes
# notes: use the BST order; if both values are larger go right, if both
#        are smaller go left, otherwise this node is the split point
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


# Iterative Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: yes
# notes: same split-point idea but walk down the tree with a loop
#        instead of recursion
class Solution2:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_val = p.val
        q_val = q.val
        node = root
        while node:
            parent_val = node.val
            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node


# Tests:
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = node4 = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = node3 = TreeNode(3)
root.left.right.right = node5 = TreeNode(5)

for sol in (Solution(), Solution2()):
    assert sol.lowestCommonAncestor(root, root.left, root.right).val == 6
    assert sol.lowestCommonAncestor(root, root.left, node4).val == 2
    assert sol.lowestCommonAncestor(root, node3, node5).val == 4
