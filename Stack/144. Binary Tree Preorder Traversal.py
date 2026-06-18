# 144. Binary Tree Preorder Traversal

# Definition for a binary tree node.
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


# Recursion Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.26: yes
# notes: visit root, then recurse left, then recurse right
class Solution:
    def preorderTraversal(self, root):
        results = []
        def preorder(root):
            if root == None:
                return
            results.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return results


# Iteration Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.26: yes
# notes: same order using an explicit queue/stack of pending nodes
class Solution2:
    def preorderTraversal(self, root):
        results = []
        nodes = []
        if root == None:
            return results
        nodes.append(root)
        while nodes:
            cur = nodes.pop(0)
            results.append(cur.val)
            if cur.left:
                nodes.append(cur.left)
            if cur.right:
                nodes.append(cur.right)
        return results


# Morris Traversal Approach:
# Time: O(n)
# Space: O(1)
# 2023.06.26: no
# notes: thread each node to its predecessor to walk without a stack
# current node cur
# 1. no left child, cur = cur.right
# 2. has left child, find rightmost node mostRight of the left subtree
# 2a. if mostRight.right is None, set it to cur, then cur = cur.left
# 2b. if mostRight.right is cur, reset it to None, cur = cur.right
# 3. stop when cur == None
class Solution3:
    def preorderTraversal(self, root):
        results = []
        if root == None:
            return results
        cur = root
        while cur != None:
            most_right = cur.left
            if most_right != None:
                while most_right.right != None and most_right.right != cur:
                    most_right = most_right.right
                if most_right.right == None:
                    results.append(cur.val)
                    most_right.right = cur
                    cur = cur.left
                    continue
                else:
                    most_right.right = None
            else:
                results.append(cur.val)
            cur = cur.right
        return results


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.preorderTraversal(build([1, None, 2, 3])) == [1, 2, 3]
    assert sol.preorderTraversal(build([3, 1, 2])) == [3, 1, 2]
    assert sol.preorderTraversal(build([])) == []
    assert sol.preorderTraversal(build([1])) == [1]
