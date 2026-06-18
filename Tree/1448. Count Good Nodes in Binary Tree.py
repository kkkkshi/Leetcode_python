# 1448. Count Good Nodes in Binary Tree

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(values):
    # level-order build; None marks a missing child
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


# Depth First Search, Recursion
# Time: O(n)
# Space: O(n)
# 2023.10.30: yes
# notes: carry the max value on the path; a node is good if it is not
#        smaller than that max
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def recursion(cur_node, max_value):
            if cur_node == None:
                return 0
            left_max = recursion(cur_node.left, max(max_value, cur_node.val))
            right_max = recursion(cur_node.right, max(max_value, cur_node.val))
            return left_max + right_max + int(cur_node.val >= max_value)
        return recursion(root, float('-inf'))


# Depth First Search, Iterative
# Time: O(n)
# Space: O(n)
# 2023.10.30: no
# notes: stack of (node, max_so_far); count when node.val >= max_so_far
class Solution2:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float("-inf"))]
        num_good_nodes = 0
        while stack:
            node, max_so_far = stack.pop()
            if max_so_far <= node.val:
                num_good_nodes += 1
            if node.left:
                stack.append((node.left, max(node.val, max_so_far)))
            if node.right:
                stack.append((node.right, max(node.val, max_so_far)))
        return num_good_nodes


# Breadth First Search
# Time: O(n)
# Space: O(n)
# 2023.10.30: no
# notes: same as dfs-iterative but with a queue
class Solution3:
    def goodNodes(self, root: TreeNode) -> int:
        num_good_nodes = 0

        # Use collections.deque for efficient popping
        queue = deque([(root, float("-inf"))])
        while queue:
            node, max_so_far = queue.popleft()
            if max_so_far <= node.val:
                num_good_nodes += 1
            if node.right:
                queue.append((node.right, max(node.val, max_so_far)))
            if node.left:
                queue.append((node.left, max(node.val, max_so_far)))

        return num_good_nodes


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.goodNodes(build([3, 1, 4, 3, None, 1, 5])) == 4
    assert sol.goodNodes(build([3, 3, None, 4, 2])) == 3
    assert sol.goodNodes(build([1])) == 1
