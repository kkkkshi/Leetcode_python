# 623. Add One Row to Tree

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


def level_order(root):
    res = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            res.append(None)
            continue
        res.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while res and res[-1] is None:
        res.pop()
    return res


# Depth First Search Approach
# Time: O(n)
# Space: O(n)
# 2023.07.04: yes
# notes: recurse down to depth-1; at depth 2 insert the new node as a
#        new parent on each side, else recurse into the children
class Solution:
    def addOneRow(self, root, val, depth):
        if depth == 1:
            return TreeNode(val, root, None)
        elif depth == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
        else:
            if root.left:
                self.addOneRow(root.left, val, depth-1)
            if root.right:
                self.addOneRow(root.right, val, depth-1)
        return root


# Depth First Search with stack Approach
# Time: O(n)
# Space: O(n)
# 2023.07.04: yes
# notes: iterate with a stack of (node, depth); at depth-1 splice a new
#        node above each child, keeping the old child as its child
class Solution2:
    class Node:
        def __init__(self, n, d):
            self.node = n
            self.depth = d

    def addOneRow(self, t, v, d) -> TreeNode:
        if d == 1:
            n = TreeNode(v)
            n.left = t
            return n

        stack = []
        stack.append(self.Node(t, 1))
        while stack:
            n = stack.pop()
            if n.node is None:
                continue
            if n.depth == d - 1:
                temp = n.node.left
                n.node.left = TreeNode(v)
                n.node.left.left = temp
                temp = n.node.right
                n.node.right = TreeNode(v)
                n.node.right.right = temp
            else:
                stack.append(self.Node(n.node.left, n.depth + 1))
                stack.append(self.Node(n.node.right, n.depth + 1))
        return t


# Breadth First Search Approach
# Time: O(n)
# Space: O(n)
# 2023.07.04: yes
# notes: walk levels with a queue down to depth-1, then for each node
#        there splice a new node above its left and right children
class Solution3:
    def addOneRow(self, t, v, d):
        if d == 1:
            n = TreeNode(v)
            n.left = t
            return n

        queue = deque()
        queue.append(t)
        depth = 1
        while depth < d - 1:
            temp = deque()
            while queue:
                node = queue.popleft()
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            depth += 1

        while queue:
            node = queue.popleft()
            temp = node.left
            node.left = TreeNode(v)
            node.left.left = temp
            temp = node.right
            node.right = TreeNode(v)
            node.right.right = temp

        return t


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    out = sol.addOneRow(build([4, 2, 6, 3, 1, 5]), 1, 2)
    assert level_order(out) == [4, 1, 1, 2, None, None, 6, 3, 1, 5]
    out = sol.addOneRow(build([4, 2, None, 3, 1]), 1, 3)
    assert level_order(out) == [4, 2, None, 1, 1, 3, None, None, 1]
    out = sol.addOneRow(build([1, 2, 3]), 5, 1)
    assert level_order(out) == [5, 1, None, 2, 3]
