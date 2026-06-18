# 236. Lowest Common Ancestor of a Binary Tree

class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


# Recursive Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: no
# notes: needs the children's results to decide, so it is a postorder
#        variant; if a subtree contains both p and q this node is the
#        answer, if only one side has them return that side
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recursion(root, p, q):
            if root == None:
                return None
            if root.val == p.val or root.val == q.val:
                return root
            left = recursion(root.left, p, q)
            right = recursion(root.right, p, q)
            if left != None and right != None:
                return root
            return left if left is not None else right
        return recursion(root, p, q)


# Iterative using parent pointers Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: no
# notes: record each node's parent, collect all ancestors of p into a
#        set, then walk up from q until a shared ancestor is hit
class Solution2:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q


# Iterative without parent pointers Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: no
# notes: track three states per node (both children pending, one done,
#        both done); after finding one node remember its stack depth,
#        and as the stack shrinks the recorded depth follows the LCA
class Solution3:
    BOTH_PENDING = 2
    LEFT_DONE = 1
    BOTH_DONE = 0

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [(root, Solution3.BOTH_PENDING)]
        one_node_found = False
        LCA_index = -1
        while stack:
            parent_node, parent_state = stack[-1]
            if parent_state != Solution3.BOTH_DONE:
                if parent_state == Solution3.BOTH_PENDING:
                    if parent_node == p or parent_node == q:
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            one_node_found = True
                            LCA_index = len(stack) - 1
                    child_node = parent_node.left
                else:
                    child_node = parent_node.right
                stack.pop()
                stack.append((parent_node, parent_state - 1))
                if child_node:
                    stack.append((child_node, Solution3.BOTH_PENDING))
            else:
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()
        return None


# Tests:
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = node6 = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = node4 = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

for sol in (Solution(), Solution2(), Solution3()):
    assert sol.lowestCommonAncestor(root, node6, node4).val == 5
    assert sol.lowestCommonAncestor(root, root.left, root.right).val == 3
    assert sol.lowestCommonAncestor(root, root.left, node4).val == 5
