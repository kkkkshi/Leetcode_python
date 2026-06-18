# 538. Convert BST to Greater Tree

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(values):
    # build a tree from a level-order list (None marks a missing node)
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def inorder(root):
    # collect node values left to right
    res = []
    def walk(node):
        if node:
            walk(node.left)
            res.append(node.val)
            walk(node.right)
    walk(root)
    return res


# Recursion Approach
# Time: O(n)
# Space: O(n)
# 2023.06.29: yes
# notes: reverse in-order (right, node, left) while adding a running
#        total so each node gets the sum of all greater values
class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.total = 0
        def convert(root):
            if root == None:
                return
            convert(root.right)
            self.total += root.val
            root.val = self.total
            convert(root.left)
            return root
        return convert(root)


# Interation Approach
# Time: O(n)
# Space: O(n)
# 2023.06.29: yes
# notes: iterative reverse in-order with a stack, carrying the total
class Solution2:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        stack = [root]
        total = 0
        cur = root
        root = root.right
        while stack or root != None:
            while root:
                stack.append(root)
                root = root.right
            root = stack.pop()
            total += root.val
            root.val = total
            root = root.left
        return cur


# Morris Approach
# Time: O(n)
# Space: O(1)
# 2023.06.29: no
# notes: Morris reverse in-order using temporary links, so no stack
class Solution3:
    def convertBST(self, root):
        # Get the node with the smallest value greater than this one.
        def get_successor(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ

        total = 0
        node = root
        while node is not None:
            # If there is no right subtree, then we can visit this node and
            # continue traversing left.
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            # If there is a right subtree, then there is a node that has a
            # greater value than the current one. therefore, we must traverse
            # that node first.
            else:
                succ = get_successor(node)
                # If there is no left subtree (or right subtree, because we are
                # in this branch of control flow), make a temporary connection
                # back to the current node.
                if succ.left is None:
                    succ.left = node
                    node = node.right
                # If there is a left subtree, it is a link that we created on
                # a previous pass, so we should unlink it and visit this node.
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left

        return root


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    r = build([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
    assert inorder(sol.convertBST(r)) == [36, 36, 35, 33, 30, 26, 21, 15, 8]
    assert inorder(sol.convertBST(build([0, None, 1]))) == [1, 1]
    assert sol.convertBST(build([])) is None
