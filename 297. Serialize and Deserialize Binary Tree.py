# 297. Serialize and Deserialize Binary Tree

# Depth-First Search Approach
# Time: O(n)
# Space: O(n)
# 2023.06.27: no
# notes: only DFS preorder/postorder or BFS can serialize uniquely;
#        inorder can't since the root isn't fixed, and the others
#        must record nulls to stay unique
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # Serialization
    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string

        return rserialize(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root


# Tests:
def build(values):
    """Build a tree from a level-order list with None for missing."""
    if not values or values[0] is None:
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


codec = Codec()
for values in ([1, 2, 3, None, None, 4, 5], [1], []):
    tree = build(values)
    restored = codec.deserialize(codec.serialize(tree))
    # round trip must be stable
    assert codec.serialize(restored) == codec.serialize(tree)

assert codec.serialize(build([1, 2, 3])) == '1,2,None,None,3,None,None,'
assert codec.serialize(build([])) == 'None,'
