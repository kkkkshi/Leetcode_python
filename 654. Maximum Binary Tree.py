# 654. Maximum Binary Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def to_list(root):
    # level-order serialize, trailing Nones trimmed
    out = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


# Recursion Approach
# Time: O(n^2)
# Space: O(n)
# 2023.06.27: no
# notes: find the max in the current range as the root, then
#        build left from the part before it and right from after
class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def constuct(nums, low, high):
            if low > high:
                return None
            ind, maxValue = -1, float('-inf')
            for i in range(low, high + 1):
                if maxValue < nums[i]:
                    ind = i
                    maxValue = nums[i]
            root = TreeNode(maxValue)
            # recursively build the left and right subtrees
            root.left = constuct(nums, low, ind - 1)
            root.right = constuct(nums, ind + 1, high)
            return root

        root = constuct(nums, 0, len(nums)-1)
        return root


# Tests:
for sol in (Solution(),):
    assert to_list(sol.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])) == \
        [6, 3, 5, None, 2, 0, None, None, 1]
    assert to_list(sol.constructMaximumBinaryTree([3, 2, 1])) == [3, None, 2, None, 1]
    assert to_list(sol.constructMaximumBinaryTree([1])) == [1]
