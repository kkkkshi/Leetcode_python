# 1644. Lowest Common Ancestor of a Binary Tree II

class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


# Recursive Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: no
# notes: a variant of 236; one extra step is to confirm both p and q
#        exist, which means the whole tree must be traversed
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        found = {'foundP': False, 'foundQ': False}
        res = self.find(root, p.val, q.val, found)
        if not found['foundP'] or not found['foundQ']:
            return None
        return res

    def find(self, root, val1, val2, found):
        if root is None:
            return None

        left = self.find(root.left, val1, val2, found)
        right = self.find(root.right, val1, val2, found)

        if left is not None and right is not None:
            return root

        if root.val == val1:
            found['foundP'] = True
        elif root.val == val2:
            found['foundQ'] = True

        return root if root.val == val1 or root.val == val2 else left or right


# Depth First Search - 2/3 Conditions Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: no
# notes: brilliant; meeting two of three conditions is enough: 1. node
#        is p or q, 2. p or q is in the left tree, 3. p or q is in the
#        right tree. If met return the node, else return left or right
#        since one side may have matched. Reaching root with nothing
#        means None
class Solution2:
    def lowestCommonAncestor(self, root, p, q):
        self.nodes_found = False

        def dfs(node):
            if not node:
              return node
            left, right = dfs(node.left), dfs(node.right)
            conditions = 0
            if node in (p, q):
              conditions += 1
            if left:
              conditions += 1
            if right:
              conditions += 1
            if conditions == 2:
              self.nodes_found = True

            if (left and right) or node in (p, q): return node
            return left or right

        ans = dfs(root)
        return ans if self.nodes_found else None


# Tests:
for sol in (Solution(), Solution2()):
    root = TreeNode(3)
    root.left = n5 = TreeNode(5)
    root.right = n1 = TreeNode(1)
    root.left.left = n6 = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = n7 = TreeNode(7)
    root.left.right.right = n4 = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    assert sol.lowestCommonAncestor(root, n5, n1) is root
    assert sol.lowestCommonAncestor(root, n5, n4) is n5
    assert sol.lowestCommonAncestor(root, n6, n7) is n5
    # q is not in the tree, so there is no common ancestor
    assert sol.lowestCommonAncestor(root, n5, TreeNode(99)) is None
