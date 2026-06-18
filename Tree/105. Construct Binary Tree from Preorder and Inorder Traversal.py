# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(node):
    # preorder traversal -> list of values
    if node is None:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)


def inorder(node):
    # inorder traversal -> list of values
    if node is None:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


# Recursion Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.27: no
# notes: harder variant of 654, same idea: the first preorder value is the
#        root, split inorder around it into left and right and recurse. a
#        hash table gives quick index lookups since values are unique.
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        valToIndex = {}
        for i in range(len(inorder)):
            valToIndex[inorder[i]] = i

        def build(preorder, preStart, preEnd, inorder, inStart, inEnd):
            if preStart > preEnd:
                return None

            # the root value is the first element of the preorder array
            rootVal = preorder[preStart]
            # index of rootVal in the inorder array
            index = valToIndex.get(rootVal)

            leftSize = index - inStart

            # build the current root node first
            root = TreeNode(rootVal)

            # recursively build the left and right subtrees
            root.left = build(preorder, preStart + 1, preStart + leftSize,
                              inorder, inStart, index - 1)

            root.right = build(preorder, preStart + leftSize + 1, preEnd,
                               inorder, index + 1, inEnd)
            return root
        return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


# Recursion Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.27: no
# notes: official answer, very concise and avoids index arithmetic by
#        walking a shared preorder_index pointer.
class Solution2:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)


# Tests:
for sol in (Solution(), Solution2()):
    t = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert preorder(t) == [3, 9, 20, 15, 7]
    assert inorder(t) == [9, 3, 15, 20, 7]
    t = sol.buildTree([-1], [-1])
    assert preorder(t) == [-1] and inorder(t) == [-1]
    assert sol.buildTree([], []) is None
