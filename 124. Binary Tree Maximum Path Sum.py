# 124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# depth-first Search Approach bottom up
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
# notes: post-order; at each node track the best path through it and
#        return the best single downward branch to the parent
class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recursion(root):
            if root == None:
                return None
            left_result = recursion(root.left)
            right_result = recursion(root.right)
            if left_result != None and right_result != None:
                self.max_value = max(left_result, right_result, left_result+right_result+root.val,
                                     max(left_result,right_result)+root.val, root.val,
                                     self.max_value)
                return max(max(left_result, right_result) + root.val, root.val)
            elif left_result == None and right_result:
                self.max_value = max(right_result, right_result + root.val, root.val, self.max_value)
                return max(right_result + root.val, root.val)
            elif right_result == None and left_result:
                self.max_value = max(left_result, left_result + root.val, root.val, self.max_value)
                return max(left_result + root.val, root.val)
            else:
                self.max_value = max(root.val, self.max_value)
                return root.val
        self.max_value = float("-inf")
        recursion(root)
        return self.max_value


# depth-first Search Approach bottom up(best approach)
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
# notes: same idea written cleaner; the trick is to never add a
#        negative subtree gain (clamp it to 0)
class Solution2:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_path = -float('inf')
        def gain_from_subtree(node):
            nonlocal max_path
            if not node:
                return 0
            gain_from_left = max(gain_from_subtree(node.left), 0)
            gain_from_right = max(gain_from_subtree(node.right), 0)
            max_path = max(max_path, gain_from_left + gain_from_right + node.val)
            return max(
                gain_from_left + node.val,
                gain_from_right + node.val
            )

        gain_from_subtree(root)
        return max_path


def build(vals):
    # level-order build; None means no node
    if not vals:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.maxPathSum(build([1, 2, 3])) == 6
    assert sol.maxPathSum(build([-10, 9, 20, None, None, 15, 7])) == 42
    assert sol.maxPathSum(build([-3])) == -3
    assert sol.maxPathSum(build([2, -1, -2])) == 2
