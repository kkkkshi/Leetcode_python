# 559. Maximum Depth of N-ary Tree

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.01: yes
# notes: BFS carrying each node's level, keep the largest level seen
class Solution:
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        max_depth = 0
        stack = [(1, root)]
        while stack:
            current_level, node = stack.pop(0)
            max_depth = max(max_depth, current_level)
            if node.children:
                for child in node.children:
                    stack.append((current_level+1, child))
        return max_depth


# Tests:
tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
for sol in (Solution(),):
    assert sol.maxDepth(tree) == 3
    assert sol.maxDepth(Node(1)) == 1
    assert sol.maxDepth(None) == 0
