# 662. Maximum Width of Binary Tree


from collections import deque


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


# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.01: no
# notes: index each node as if the tree were complete, then the
#        width of a level is last index minus first index plus 1
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        max_width = 0
        queue = deque()
        queue.append((root, 0))
        while queue:
            level_length = len(queue)
            _, level_head_index = queue[0]
            # iterate through the current level
            for _ in range(level_length):
                node, col_index = queue.popleft()
                # preparing for the next level
                if node.left:
                    queue.append((node.left, 2 * col_index))
                if node.right:
                    queue.append((node.right, 2 * col_index + 1))
            # calculate the length of the current level,
            #   by comparing the first and last col_index.
            max_width = max(max_width, col_index - level_head_index + 1)
        return max_width


# depth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.01: no
# notes: preorder DFS recording the first column index per depth,
#        width is current column minus that first one plus 1
class Solution2:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        # table contains the first col_index for each level
        first_col_index_table = {}
        max_width = 0
        def DFS(node, depth, col_index):
            nonlocal max_width
            if node is None:
                return
            # if the entry is empty, set the value
            if depth not in first_col_index_table:
                first_col_index_table[depth] = col_index
            max_width = max(max_width, col_index - first_col_index_table[depth] + 1)
            # Preorder DFS, with the priority on the left child
            DFS(node.left, depth+1, 2*col_index)
            DFS(node.right, depth+1, 2*col_index + 1)
        DFS(root, 0, 0)
        return max_width


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.widthOfBinaryTree(build([1, 3, 2, 5, 3, None, 9])) == 4
    assert sol.widthOfBinaryTree(build([1, 3, 2, 5, None, None, 9, 6, None, 7])) == 7
    assert sol.widthOfBinaryTree(build([1, 3, 2, 5])) == 2
    assert sol.widthOfBinaryTree(build([1])) == 1
