# 637. Average of Levels in Binary Tree

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
    queue = deque([root])
    for val in it:
        node = queue[0]
        if node.left is None:
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
        else:
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)
            queue.popleft()
    return root


# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: yes
# notes: process the tree level by level; sum each level's values and
#        divide by the level size to get its average
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s = []
        results = []
        if root == None:
            return s
        s.append(root)
        while s:
            current_value = 0
            current_level = len(s)
            for i in range(current_level):
                node = s.pop(0)
                current_value += node.val
                if node.right:
                    s.append(node.right)
                if node.left:
                    s.append(node.left)
            current_value /= current_level
            results.append(current_value)
        return results


# Tests:
for sol in (Solution(),):
    assert sol.averageOfLevels(build([3, 9, 20, None, None, 15, 7])) == [3, 14.5, 11]
    assert sol.averageOfLevels(build([2, 2, 2])) == [2, 2]
    assert sol.averageOfLevels(build([5])) == [5]
