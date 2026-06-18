# 652. Find Duplicate Subtrees

# A String Representation Approach
# Time: O(n^2)
# Space: O(n^2)
# 2023.06.27: no
# notes: serialize each subtree to a string and record duplicates the
#        moment a serialization is seen a second time
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    if not node:
        return "#"
    return str(node.val) + "," + serialize(node.left) + "," + serialize(node.right)


class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def traverse(node):
            if not node:
                return ""
            representation = ("(" + traverse(node.left) + ")" + str(node.val)
                              + "(" + traverse(node.right) + ")")
            cnt[representation] += 1
            if cnt[representation] == 2:
                res.append(node)
            return representation
        cnt = collections.defaultdict(int)
        res = []
        traverse(root)
        return res


# An Optimized Approach
# Time: O(n)
# Space: O(n)
# 2023.06.27: no
# notes: represent each subtree as a triplet and give it an id; reusing
#        an id means the subtree repeated, so one id stands for one
#        unique subtree shape
class Solution2:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def traverse(node):
            if not node:
                return 0
            triplet = (traverse(node.left), node.val, traverse(node.right))
            if triplet not in triplet_to_id:
                triplet_to_id[triplet] = len(triplet_to_id) + 1
            id = triplet_to_id[triplet]
            cnt[id] += 1
            if cnt[id] == 2:
                res.append(node)
            return id
        triplet_to_id = dict()
        cnt = collections.defaultdict(int)
        res = []
        traverse(root)
        return res


# Tests:
t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(4)
t.right = TreeNode(3)
t.right.left = TreeNode(2)
t.right.left.left = TreeNode(4)
t.right.right = TreeNode(4)
for sol in (Solution(), Solution2()):
    dups = sorted(serialize(node) for node in sol.findDuplicateSubtrees(t))
    assert dups == ["2,4,#,#,#", "4,#,#"]
    assert sol.findDuplicateSubtrees(TreeNode(1)) == []
    leaf = TreeNode(1, TreeNode(1), TreeNode(1))
    dups2 = sorted(serialize(node) for node in sol.findDuplicateSubtrees(leaf))
    assert dups2 == ["1,#,#"]
