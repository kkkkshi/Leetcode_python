# 617. Merge Two Binary Trees

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(vals):
    if not vals:
        return None
    it = iter(vals)
    root = TreeNode(next(it))
    q = deque([root])
    while q:
        node = q.popleft()
        try:
            v = next(it)
        except StopIteration:
            break
        if v is not None:
            node.left = TreeNode(v)
            q.append(node.left)
        try:
            v = next(it)
        except StopIteration:
            break
        if v is not None:
            node.right = TreeNode(v)
            q.append(node.right)
    return root


def serialize(root):
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        n = q.popleft()
        if n:
            res.append(n.val)
            q.append(n.left)
            q.append(n.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res


# Recursion Approach
# Time: O(n)
# Space: O(n)
# 2023.06.29: yes
# notes: add the two node values, then merge left and right
#        subtrees; if one tree is missing, keep the other
class Solution:
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 == None and root2 == None:
            return None
        elif root1 == None:
            return root2
        elif root2 == None:
            return root1
        root1.val = root1.val + root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


# Iteration Approach
# Time: O(n)
# Space: O(n)
# 2023.06.29: yes
# notes: walk both trees with a stack; when one child is None,
#        attach the other tree's child directly
class Solution2:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        stack = [(t1, t2)]
        while stack:
            t = stack.pop()
            if t[0] is None or t[1] is None:
                continue
            t[0].val += t[1].val
            if t[0].left is None:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left, t[1].left))
            if t[0].right is None:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right, t[1].right))
        return t1


# Tests:
for sol in (Solution(), Solution2()):
    r = sol.mergeTrees(build([1, 3, 2, 5]),
                       build([2, 1, 3, None, 4, None, 7]))
    assert serialize(r) == [3, 4, 5, 5, 4, None, 7]
    assert serialize(sol.mergeTrees(build([1]), build([1, 2]))) == [2, 2]
    assert serialize(sol.mergeTrees(None, build([1]))) == [1]
