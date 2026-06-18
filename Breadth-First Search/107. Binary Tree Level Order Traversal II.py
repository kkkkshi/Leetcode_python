# 107. Binary Tree Level Order Traversal II

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: yes
# notes: BFS level by level, inserting each level at the front so
#        the bottom level ends up first
class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        s = []
        level_nodes = []
        results = []
        if root == None:
            return s
        s.append(root)
        while s:
            current_level = len(s)
            for i in range(current_level):
                node = s.pop(0)
                level_nodes.append(node.val)
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)
            results.insert(0,level_nodes)
            level_nodes = []
        return results


# depth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: yes
# notes: DFS carrying the depth; append values per level then
#        reverse the level list at the end
class Solution2:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels

        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels[::-1]


# Tests:
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
for sol in (Solution(), Solution2()):
    assert sol.levelOrderBottom(tree) == [[15, 7], [9, 20], [3]]
    assert sol.levelOrderBottom(None) == []
    assert sol.levelOrderBottom(TreeNode(1)) == [[1]]
