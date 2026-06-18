# 95. Unique Binary Search Trees II

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    if not node:
        return None
    return (node.val, serialize(node.left), serialize(node.right))


def shapes(trees):
    return sorted((serialize(t) for t in trees), key=str)


# Recursive Dynamic Programming Approach
# Time: complicated
# Space: complicated
# 2023.06.30: no
# notes: pick each value as the root, recursively build all left and
#        right subtrees, then combine every left/right pair; memoize by
#        (start, end) range
class Solution:
    def allPossibleBST(self, start, end, memo):
        res = []
        if start > end:
            res.append(None)
            return res
        if (start, end) in memo:
            return memo[(start, end)]

        # Iterate through all values from start to end to construct left and right subtree recursively.
        for i in range(start, end + 1):
            leftSubTrees = self.allPossibleBST(start, i - 1, memo)
            rightSubTrees = self.allPossibleBST(i + 1, end, memo)

            # Loop through all left and right subtrees and connect them to ith root.
            for left in leftSubTrees:
                for right in rightSubTrees:
                    root = TreeNode(i, left, right)
                    res.append(root)

        memo[(start, end)] = res
        return res

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        memo = {}
        return self.allPossibleBST(1, n, memo)


# Iterative Dynamic Programming
# Time: complicated
# Space: complicated
# 2023.06.30: no
# notes: bottom-up over subtree size; dp[start][end] holds every BST on
#        that value range, built by combining smaller ranges
class Solution2:
    def generateTrees(self, n: int):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        dp = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][i] = [TreeNode(i)]

        for numberOfNodes in range(2, n + 1):
            for start in range(1, n - numberOfNodes + 2):
                end = start + numberOfNodes - 1
                for i in range(start, end + 1):
                    left_subtrees = dp[start][i - 1] if i != start else [None]
                    right_subtrees = dp[i + 1][end] if i != end else [None]

                    for left in left_subtrees:
                        for right in right_subtrees:
                            root = TreeNode(i, left, right)
                            dp[start][end].append(root)

        return dp[1][n]


# Dynamic Programming with Space Optimization
# Time: complicated
# Space: complicated
# 2023.06.30: no
# notes: only track trees by node count; reuse smaller results and
#        clone the right subtree with a value offset to shift its range
class Solution3:
    def generateTrees(self, n: int):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        dp = [[] for _ in range(n + 1)]
        dp[0].append(None)

        for numberOfNodes in range(1, n + 1):
            for i in range(1, numberOfNodes + 1):
                j = numberOfNodes - i
                for left in dp[i - 1]:
                    for right in dp[j]:
                        root = TreeNode(i, left, self.clone(right, i))
                        dp[numberOfNodes].append(root)

        return dp[n]

    def clone(self, node, offset: int):
        if not node:
            return None
        cloned_node = TreeNode(node.val + offset)
        cloned_node.left = self.clone(node.left, offset)
        cloned_node.right = self.clone(node.right, offset)
        return cloned_node


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert shapes(sol.generateTrees(1)) == [(1, None, None)]
    assert len(sol.generateTrees(2)) == 2
    assert len(sol.generateTrees(3)) == 5
