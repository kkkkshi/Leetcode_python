# 653. Two Sum IV - Input is a BST


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(values):
    # level-order build, None means no node
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


# Depth First Search Approach
# Time: O(n)
# Space: O(n)
# 2023.07.04: yes
# notes: inorder traversal gives a sorted list, then use two
#        pointers from both ends to look for a pair summing to k
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def inorder(root, values):
            if root is None:
                return
            inorder(root.left, values)
            values.append(root.val)
            inorder(root.right, values)

        values = []
        inorder(root, values)
        left, right = 0, len(values) - 1
        while left < right:
            total = values[left] + values[right]
            if total == k:
                return True
            elif total < k:
                left += 1
            else:
                right -= 1
        return False


# Tests:
for sol in (Solution(),):
    tree = build([5, 3, 6, 2, 4, None, 7])
    assert sol.findTarget(tree, 9) is True
    assert sol.findTarget(tree, 28) is False
    assert sol.findTarget(build([2, 1, 3]), 4) is True
    assert sol.findTarget(build([2, 1, 3]), 5) is True
    assert sol.findTarget(build([1]), 2) is False
