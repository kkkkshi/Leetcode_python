# 103. Binary Tree Zigzag Level Order Traversal

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
# 2023.07.02: yes
class Solution:
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
for sol in (Solution(), Solution2()):
    assert [list(x) for x in
            sol.zigzagLevelOrder(build([3, 9, 20, None, None, 15, 7]))] == \
        [[3], [20, 9], [15, 7]]
    assert [list(x) for x in sol.zigzagLevelOrder(build([1]))] == [[1]]
    assert [list(x) for x in sol.zigzagLevelOrder(build([]))] == []
