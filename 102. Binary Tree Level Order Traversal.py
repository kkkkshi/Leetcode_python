# 102. Binary Tree Level Order Traversal

from collections import deque


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


# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.01: yes
# notes: double loop, one over the queue and one over each level; before
#        moving to the next level, count the current queue size.
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if root == None:
            return levels
        level = 0
        q = [root]
        while q:
            levels.append([])
            level_length = len(q)
            for i in range(level_length):
                node = q.pop(0)
                levels[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return levels


# depth-first Approach
# Time: O(n^2)
# Space: O(1)
# 2023.07.01: yes
# notes: track the level and append a new [] when reaching a new level
class Solution2:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if root == None:
            return levels
        def node_recursion(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                node_recursion(node.left, level+1)
            if node.right:
                node_recursion(node.right, level+1)
        node_recursion(root, 0)
        return levels


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.levelOrder(build([3, 9, 20, None, None, 15, 7])) == \
        [[3], [9, 20], [15, 7]]
    assert sol.levelOrder(build([1])) == [[1]]
    assert sol.levelOrder(build([])) == []
