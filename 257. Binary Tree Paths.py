# 257. Binary Tree Paths

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(values):
    # build a tree from a level-order list, using None for gaps
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


# depth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: yes
# notes: walk down carrying the path string; when a leaf is hit,
#        save the path; otherwise append '->' and recurse
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # if reach a leaf
                    paths.append(path)  # update paths
                else:
                    path += '->'  # extend the current path
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths


# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: yes
# notes: same idea iteratively; carry (node, path) on a stack and
#        push children with the extended path until leaves are found
class Solution2:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))

        return paths


# Tests:
for sol in (Solution(), Solution2()):
    assert sorted(sol.binaryTreePaths(build([1, 2, 3, None, 5]))) == \
        ['1->2->5', '1->3']
    assert sol.binaryTreePaths(build([1])) == ['1']
    assert sol.binaryTreePaths(build([])) == []
    assert sorted(sol.binaryTreePaths(build([1, 2, 3]))) == \
        ['1->2', '1->3']
