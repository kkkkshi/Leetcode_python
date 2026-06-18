# 230. Kth Smallest Element in a BST

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(values):
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


# Recursive Inorder Traversal Approach
# Time: O(n)
# Space: O(n)
# 2023.06.28: yes
# notes: inorder traversal of a BST is sorted, so take the (k-1)th
#        element of the inorder list
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]


# Iterative Inorder Traversal Approach
# Time: O(H+k)
# Space: O(H)
# 2023.06.28: no
# notes: walk left pushing nodes, pop in sorted order, stop after the
#        kth pop
class Solution2:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.kthSmallest(build([3, 1, 4, None, 2]), 1) == 1
    assert sol.kthSmallest(build([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
    assert sol.kthSmallest(build([5, 3, 6, 2, 4, None, None, 1]), 6) == 6
