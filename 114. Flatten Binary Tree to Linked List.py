# 114. Flatten Binary Tree to Linked List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def to_list(root):
    # walk the right spine after flattening
    res = []
    while root:
        res.append(root.val)
        assert root.left is None
        root = root.right
    return res


def build_sample():
    r = TreeNode(5)
    r.left = TreeNode(2)
    r.left.right = TreeNode(6)
    r.left.right.left = TreeNode(44)
    r.left.right.left.right = TreeNode(23)
    r.right = TreeNode(1)
    r.right.left = TreeNode(10)
    r.right.right = TreeNode(11)
    return r


# Recursion Approach
# Time: O(n)
# Space: O(n)
# 2023.06.26: no
# notes: the work is in the post-order spot: after flattening both
#        sides, splice the left chain in, then attach the old right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        # base case
        if not root:
            return
        # flatten left and right subtrees per the definition
        self.flatten(root.left)
        self.flatten(root.right)
        # post-order position
        # 1. left and right subtrees are now single chains
        left = root.left
        right = root.right
        # 2. move the left subtree to the right
        root.left = None
        root.right = left
        # 3. append the old right subtree to the new tail
        p = root
        while p.right:
            p = p.right
        p.right = right


# Iterative Solution using Stack Approach
# Time: O(n)
# Space: O(n)
# 2023.06.26: no
# notes: two states start/end; end means the left side is ordered,
#        start means it still needs work. On start with a left child,
#        re-push the node as end and push the left child first.
#        The left pops first, ends up with no left child, so it is
#        end. On start without a left child, push the right child.
#        Before reaching a tail node there is no tailNode, so keep
#        pushing unordered nodes until a tail appears, then wire
#        them back from tail to head. The rest is joining head and
#        tail via the stack, picking the tail whose right links to
#        the head's right subtree
import collections

class Solution2:

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Handle the null scenario
        if not root:
            return None

        START, END = 1, 2

        tailNode = None
        stack = collections.deque([(root, START)])

        while stack:

            currentNode, recursionState = stack.pop()

            # We reached a leaf node. Record this as a tail
            # node and move on.
            if not currentNode.left and not currentNode.right:
                tailNode = currentNode
                continue

            # If the node is in the START state, it means we still
            # haven't processed it's left child yet.
            if recursionState == START:

                # If the current node has a left child, we add it
                # to the stack AFTER adding the current node again
                # to the stack with the END recursion state.
                if currentNode.left:
                    stack.append((currentNode, END))
                    stack.append((currentNode.left, START))
                elif currentNode.right:

                    # In case the current node didn't have a left child
                    # we will add it's right child
                    stack.append((currentNode.right, START))
            else:
                # If the current node is in the END recursion state,
                # that means we did process one of it's children. Left
                # if it existed, else right.
                rightNode = currentNode.right

                # If there was a left child, there must have been a leaf
                # node and so, we would have set the tailNode
                if tailNode:
                    # Establish the proper connections.
                    tailNode.right = currentNode.right
                    currentNode.right = currentNode.left
                    currentNode.left = None
                    rightNode = tailNode.right

                if rightNode:
                    stack.append((rightNode, START))


# O(1) Iterative Solution Approach
# Time: O(n)
# Space: O(1)
# 2023.06.26: no
# notes: very like Morris traversal; if there is a left subtree, find
#        its rightmost node (no right child, maybe a left), attach the
#        node's right subtree there, so the node keeps only a left
#        subtree; make the left the right, move on and repeat; with no
#        left subtree, just step into the right child
class Solution3:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Handle the null scenario
        if not root:
            return None
        node = root
        while node:
            # If the node has a left child
            if node.left:
                # Find the rightmost node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            # move on to the right side of the tree
            node = node.right


# Tests:
expected = [5, 2, 6, 44, 23, 1, 10, 11]
for sol in (Solution(), Solution2(), Solution3()):
    r = build_sample()
    sol.flatten(r)
    assert to_list(r) == expected
