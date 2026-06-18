# 106. Construct Binary Tree from Inorder and Postorder Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def to_list(root):
    # level-order serialization with trailing None trimmed
    res = []
    q = [root]
    while q:
        node = q.pop(0)
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res


# Recursion Approach
# Time: O(n)
# Space: O(n)
# 2023.06.27: yes
# notes: adapted from 105; read postorder right to left, so build
#        the right subtree before the left one
class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.postorder_index = len(postorder) -1
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        def array_to_tree(left, right):
            if left > right: return None
            root_value = postorder[self.postorder_index]
            root = TreeNode(root_value)
            self.postorder_index -= 1
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            return root
        return array_to_tree(0, len(postorder) - 1)


# Tests:
for sol in (Solution(),):
    assert to_list(sol.buildTree([9, 3, 15, 20, 7],
                                 [9, 15, 7, 20, 3])) == [3, 9, 20, None, None, 15, 7]
    assert to_list(sol.buildTree([-1], [-1])) == [-1]
    assert to_list(sol.buildTree([2, 1], [2, 1])) == [1, 2]
