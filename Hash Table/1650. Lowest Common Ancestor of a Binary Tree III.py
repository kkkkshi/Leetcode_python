# 1650. Lowest Common Ancestor of a Binary Tree III

class TreeNode:
    def __init__(self, x, left = None, right = None, parent = None):
        self.val = x
        self.left = left
        self.right = right
        self.parent = parent


# Iterative Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: yes
# notes: walk p up to the root storing every ancestor, then walk q up
#        until it hits a node already on p's path
class Solution:
    def lowestCommonAncestor(self, p, q):
        path = set()
        while p:
            path.add(p)
            p = p.parent
        while q not in path:
            q = q.parent
        return q


# Two Pointers Approach
# Time: O(n)
# Space: O(1)
# notes: it is just a linked-list problem; chain p then q, q then p,
#        and a shared node is always met, otherwise it is the root
class Solution2:
    def lowestCommonAncestor(self, p, q):
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
        return p1


# Tests:
for sol in (Solution(), Solution2()):
    tree = TreeNode(3)
    tree.left = n5 = TreeNode(5)
    tree.right = n1 = TreeNode(1)

    tree.left.left = n6 = TreeNode(6)
    tree.left.left.parent = tree.left
    tree.left.right = n2 = TreeNode(2)
    tree.left.right.parent = tree.left
    tree.left.parent = tree

    tree.right.left = n0 = TreeNode(0)
    tree.right.left.parent = tree.right
    tree.right.right = n8 = TreeNode(8)
    tree.right.right.parent = tree.right
    tree.right.parent = tree

    assert sol.lowestCommonAncestor(n1, n8) is n1
    assert sol.lowestCommonAncestor(n6, n2) is n5
    assert sol.lowestCommonAncestor(n6, n8) is tree
    assert sol.lowestCommonAncestor(n5, n5) is n5
