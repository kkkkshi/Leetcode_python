# 100. Same Tree

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(values):
    # level-order list -> tree, None marks a missing node
    if not values:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


# depth-first Search Approach (best approach)
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def recursion(p, q):
            if p.left and q.left:
                left = recursion(p.left, q.left)
            elif p.left or q.left:
                left = False
            else:
                left = True
            if p.right and q.right:
                right = recursion(p.right, q.right)
            elif p.right or q.right:
                right = False
            else:
                right = True
            if p.val == q.val:
                cur = True
            else:
                cur = False
            return left and right and cur
        if p == None and q == None:
            return True
        elif p and q:
            return recursion(p, q)
        else:
            return False


# depth-first Search Approach (best approach)
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
# notes: same method as above, just written more concisely
class Solution2:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)


# breadth-first Search Approach (best approach)
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
class Solution3:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True

        deq = deque([(p, q), ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.isSameTree(build([1, 2, 3]), build([1, 2, 3])) == True
    assert sol.isSameTree(build([1, 2]), build([1, None, 2])) == False
    assert sol.isSameTree(build([1, 2, 1]), build([1, 1, 2])) == False
    assert sol.isSameTree(build([]), build([])) == True
    assert sol.isSameTree(build([1]), build([])) == False
