# 515. Find Largest Value in Each Tree Row

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


# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: yes
# notes: level-order walk; keep the max value seen at each level
class Solution:
    def largestValues(self, root):
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
            max_current = float('-inf')
            current_level = len(s)
            for i in range(current_level):
                node = s.pop(0)
                max_current = max(max_current, node.val)
                if node.right:
                    s.append(node.right)
                if node.left:
                    s.append(node.left)
            results.append(max_current)
        return results


# Tests:
for sol in (Solution(),):
    assert sol.largestValues(build([1, 3, 2, 5, 3, None, 9])) == [1, 3, 9]
    assert sol.largestValues(build([1, 2, 3])) == [1, 3]
    assert sol.largestValues(build([])) == []
    assert sol.largestValues(build([-1, -2, -3])) == [-1, -2]
