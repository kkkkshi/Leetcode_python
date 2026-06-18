# 700. Search in a Binary Search Tree

from collections import deque


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


def to_list(root):
    if root is None:
        return []
    res, q = [], deque([root])
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res


# Recursive Algorithm (best approach)
# Time: O(h)
# Space: O(h)
# 2023.06.29: yes
# notes: walk down the BST, going left/right by comparing val
class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def dfs(root, val):
            if root == None:
                return None
            if val == root.val:
                return root
            if val < root.val:
                left = dfs(root.left, val)
                if left != None:
                    return left
            if val > root.val:
                right = dfs(root.right, val)
                if right != None:
                    return right
        return dfs(root, val)


# Iteration Algorithm (best approach)
# Time: O(h)
# Space: O(1)
# 2023.06.29: yes
# notes: same walk done with a loop instead of recursion
class Solution2:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root


# Tests:
for sol in (Solution(), Solution2()):
    tree = build([4, 2, 7, 1, 3])
    assert to_list(sol.searchBST(tree, 2)) == [2, 1, 3]
    assert to_list(sol.searchBST(tree, 7)) == [7]
    assert to_list(sol.searchBST(tree, 5)) == []
