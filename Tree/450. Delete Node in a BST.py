# 450. Delete Node in a BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursion Approach
# Time: O(logn)
# Space: O(h)
# 2023.06.30: no
# notes: the call returns the subtree after deletion, so always
#        reassign it back
class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def minLeft(root):
            while root.left:
                root = root.left
            return root
        if root == None:
            return None
        if root.val == key:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            minLeftNode = minLeft(root.right)
            # delete the smallest node in the right tree; this
            # returns the right tree after deletion
            root.right = self.deleteNode(root.right, minLeftNode.val)
            # could also just overwrite the value, but in practice
            # it is better not to rely on internal values, so swap
            # the node instead
            minLeftNode.left = root.left
            minLeftNode.right = root.right
            root = minLeftNode
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


# Tests:
for sol in (Solution(),):
    tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)),
                    TreeNode(6, None, TreeNode(7)))
    res = sol.deleteNode(tree, 3)
    assert inorder(res) == [2, 4, 5, 6, 7]

    leaf = TreeNode(5)
    assert sol.deleteNode(leaf, 5) is None

    single = TreeNode(5)
    assert inorder(sol.deleteNode(single, 9)) == [5]
