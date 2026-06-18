# 222. Count Complete Tree Nodes

class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


def build(values):
    """Build a tree from a level-order list (None for missing)."""
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


# Recursive Approach
# Time: O(log^2 n)
# Space: O(1)
# 2023.07.02: no
# notes: the plain way is to count every node, but the trick below
# is faster: a complete tree is a full tree plus a complete subtree;
# count the full part, then recurse into the remaining complete tree
class Solution:
    def countNodes(self, root):
        l = root
        r = root
        hl = 0
        hr = 0

        # Calculate the height along the leftmost path
        while l is not None:
            l = l.left
            hl += 1

        # Calculate the height along the rightmost path
        while r is not None:
            r = r.right
            hr += 1

        # If the heights are equal, it is a complete binary tree
        if hl == hr:
            return 2 ** hl - 1

        # If the heights are not equal, calculate recursively
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# Recursive Approach
# Time: O(log^2 n)
# Space: O(1)
# 2023.07.02: no
# notes: binary search the last level to see which of its nodes exist
class Solution3:
    def compute_depth(self, node: TreeNode) -> int:
        """
        Return tree depth in O(d) time.
        """
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists.
        Binary search with O(d) complexity.
        """
        left, right = 0, 2 ** d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None

    def countNodes(self, root: TreeNode) -> int:
        # if the tree is empty
        if not root:
            return 0

        d = self.compute_depth(root)
        # if the tree contains 1 node
        if d == 0:
            return 1

        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        left, right = 1, 2 ** d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1

        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        return (2 ** d - 1) + left


# Tests:
for sol in (Solution(), Solution3()):
    assert sol.countNodes(build([1, 2, 3, 4, 5, 6])) == 6
    assert sol.countNodes(build([])) == 0
    assert sol.countNodes(build([1])) == 1
    assert sol.countNodes(build([1, 2, 3, 4, 5, 6, 7])) == 7
