# 671. Second Minimum Node In a Binary Tree

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
            node.left = TreeNode(val)
            queue.append(node.left)
        else:
            node.right = TreeNode(val)
            queue.append(node.right)
            queue.popleft()
    return root


# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.01: no
# notes: root is the global min; search for the smallest value strictly
#        greater than it, recursing only into nodes equal to the min
class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = float('inf')
        min1 = root.val
        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.ans if self.ans < float('inf') else -1


# Tests:
for sol in (Solution(),):
    assert sol.findSecondMinimumValue(build([2, 2, 5, 5, 7])) == 5
    assert sol.findSecondMinimumValue(build([2, 2, 2])) == -1
    assert sol.findSecondMinimumValue(build([1, 1, 3, 1, 1, 3, 4])) == 3
