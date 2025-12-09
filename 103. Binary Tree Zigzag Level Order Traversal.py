class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: yes
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        s = []
        level_nodes = []
        results = []
        reversed = True
        if root == None:
            return s
        s.append(root)
        while s:
            current_level = len(s)
            for i in range(current_level):
                node = s.pop(0)
                if reversed:
                    level_nodes.append(node.val)
                else:
                    level_nodes.insert(0, node.val)
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)
            reversed = not reversed
            results.append(level_nodes)
            level_nodes = []
        return results


# depth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: yes
from collections import deque

class Solution2:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        results = []
        def dfs(node, level):
            if level >= len(results):
                results.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    results[level].append(node.val)
                else:
                    results[level].appendleft(node.val)

            for next_node in [node.left, node.right]:
                if next_node is not None:
                    dfs(next_node, level+1)
        dfs(root, 0)

        return results

# Tests:
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
tree2 = TreeNode(0, TreeNode(2, TreeNode(1, TreeNode(5), TreeNode(1)), None),
                 TreeNode(4, TreeNode(3, None, TreeNode(6)), TreeNode(-1, None, TreeNode(8))))
test = Solution()
test.zigzagLevelOrder(tree2)