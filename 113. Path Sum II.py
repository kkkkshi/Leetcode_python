# 113. Path Sum II

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# depth-first Search Approach bottom up
# Time: O(n)
# Space: O(n), when unbalanced
# 2023.07.03: yes
# notes: backtrack down each root-to-leaf path tracking the current
#        list; record a copy whenever a leaf hits the target
class Solution:
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        def recursion(root, targetSum, cur):
            if root == None:
                return
            if root.left == None and root.right == None:
                if targetSum - root.val == 0:
                    cur.append(root.val)
                    results.append(cur[:])
                    cur.pop()
                    return
                else:
                    return
            cur.append(root.val)
            recursion(root.left, targetSum-root.val, cur)
            recursion(root.right, targetSum-root.val, cur)
            cur.pop()
        results = []
        recursion(root, targetSum, [])
        return results


# Tests:
tree = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None),
                TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
for sol in (Solution(),):
    assert sol.pathSum(tree, 22) == [[5, 4, 11, 2], [5, 8, 4, 5]]
    assert sol.pathSum(tree, 100) == []
    assert sol.pathSum(None, 0) == []
    assert sol.pathSum(TreeNode(1), 1) == [[1]]
