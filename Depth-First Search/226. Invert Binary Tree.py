# 226. Invert Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(values):
    """Build a tree from a level-order list (None for missing)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def to_list(root):
    """Serialize a tree to a level-order list, trimming trailing None."""
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


# Recursive Approach:
# Time: O(n)
# Space: O(h) h is the depth of the tree
# 2023.06.26: yes
# notes: swap the children of the current node, then recurse down
class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# Iterative Approach
# Time: O(n)
# Space: O(n) h is the depth of the tree
# 2023.06.26: yes
# notes: swap each node's children, push the children onto a stack
#        and keep going until it is empty
class Solution2:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        saving = [root]
        while saving:
            cur = saving.pop(-1)
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                saving.append(cur.left)
            if cur.right:
                saving.append(cur.right)
        return root


# Tests:
for sol in (Solution(), Solution2()):
    assert to_list(sol.invertTree(build([4, 2, 7, 1, 3, 6, 9]))) == \
        [4, 7, 2, 9, 6, 3, 1]
    assert to_list(sol.invertTree(build([2, 1, 3]))) == [2, 3, 1]
    assert to_list(sol.invertTree(build([]))) == []
