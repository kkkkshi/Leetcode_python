# Depth First Search, Recursion
# Time: O(n)
# Space: O(n)
# 2023.10.30: yes
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
# notes: 一层层存储，存储当前节点和max_so_far即可
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
# notes: 和dfs-iterative一样
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

# test
test = Solution2()
t1 = TreeNode(3, TreeNode(1, TreeNode(3), None), TreeNode(4, TreeNode(1), TreeNode(5)))
test.goodNodes(t1)
t2 = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
test.goodNodes(t2)
