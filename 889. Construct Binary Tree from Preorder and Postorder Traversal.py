# 889. Construct Binary Tree from Preorder and Postorder Traversal


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_level(root):
    out = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


# Recursion Approach
# Time: O(n)
# Space: O(n)
# 2023.06.27: yes
# notes: preorder gives the root; the next preorder value marks the
#        left subtree boundary via its postorder index, recurse on both
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.preorder_index = 0

        postorder_index_map = {}
        for index, value in enumerate(postorder):
            postorder_index_map[value] = index

        def array_to_tree(left, right):
            if left > right: return None
            root_value = preorder[self.preorder_index]
            root = TreeNode(root_value)
            self.preorder_index += 1
            if left == right:
                return root
            bound = preorder[self.preorder_index]
            bound2 = postorder_index_map[bound]
            root.left = array_to_tree(left, bound2)
            root.right = array_to_tree(bound2+ 1, right-1)

            return root
        return array_to_tree(0, len(postorder) - 1)


# Tests:
for sol in (Solution(),):
    assert build_level(sol.constructFromPrePost(
        [1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])) == [1, 2, 3, 4, 5, 6, 7]
    assert build_level(sol.constructFromPrePost([1], [1])) == [1]
    assert build_level(sol.constructFromPrePost(
        [1, 2, 3], [3, 2, 1])) == [1, 2, None, 3]
