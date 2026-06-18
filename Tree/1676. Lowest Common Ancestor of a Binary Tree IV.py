# 1676. Lowest Common Ancestor of a Binary Tree IV

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# Recursive Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: yes
# notes: same as 236 but match against a list of nodes; a node whose
#        left and right both return non-None is the common ancestor
class Solution:
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        :rtype: TreeNode
        """
        def recursion(root, nodes):
            if root == None:
                return None
            for node in nodes:
                if node.val == root.val:
                    return root
            left = recursion(root.left, nodes)
            right = recursion(root.right, nodes)
            if left != None and right != None:
                return root
            return left if left is not None else right
        return recursion(root, nodes)


# Tests:
for sol in (Solution(),):
    root = TreeNode(3)
    root.left = n5 = TreeNode(5)
    root.right = n1 = TreeNode(1)
    root.left.left = n6 = TreeNode(6)
    root.left.right = n2 = TreeNode(2)
    root.left.right.left = n7 = TreeNode(7)
    root.left.right.right = n4 = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = n8 = TreeNode(8)

    assert sol.lowestCommonAncestor(root, [n6, n4]) is n5
    assert sol.lowestCommonAncestor(root, [n5, n1]) is root
    assert sol.lowestCommonAncestor(root, [n7]) is n7
    assert sol.lowestCommonAncestor(root, [n6, n7, n4]) is n5
