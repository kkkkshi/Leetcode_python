# 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
from queue import LifoQueue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(values):
    # level-order build; None marks a missing child
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


# Recursion Approach
# Time: O(n)
# Space: O(n)
# 2023.06.30: yes
# notes: recurse left, recurse right, then visit root
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traversal(root):
            if root == None:
                return
            traversal(root.left)
            traversal(root.right)
            results.append(root.val)
        results = []
        traversal(root)
        return results


# Iteration Approach
# Time: O(n)
# Space: O(n)
# 2023.06.30: yes
# notes: pop a node, save it, push left then right; drain the save
#        stack at the end to reverse into postorder
class Solution2:
    def postorderTraversal(self, root):
        results = []
        post_order_stack = LifoQueue()
        post_order_save_stack = LifoQueue()
        post_order_stack.put(root)
        while (not post_order_stack.empty() and root != None):
            cur = post_order_stack.get()
            post_order_save_stack.put(cur)
            if cur.left:
                post_order_stack.put(cur.left)
            if cur.right:
                post_order_stack.put(cur.right)
        while not post_order_save_stack.empty():
            cur = post_order_save_stack.get()
            results.append(cur.val)
        return results


# Morris Approach:
# notes: thread the tree; for each subtree with a left child, print the
#        reversed right edge of that left subtree, then the root's edge
class Solution3:
    def postorderTraversal(self, root):
        self.result = []
        if root == None:
            return self.result
        cur = root
        while cur != None:
            most_right = cur.left
            if most_right != None:  # there is left tree
                while most_right.right != None and most_right.right != cur:
                    most_right = most_right.right
                if most_right.right == None:
                    most_right.right = cur
                    cur = cur.left
                    continue
                else:
                    most_right.right = None
                    self.print_edge(cur.left)
            cur = cur.right  # no left tree
        self.print_edge(root)
        return self.result

    def print_edge(self, root):
        tail = self.reverse_edge(root)
        cur = tail
        while cur:
            self.result.append(cur.val)
            cur = cur.right
        self.reverse_edge(tail)

    def reverse_edge(self, head):
        pre = None
        while head:
            next = head.right
            head.right = pre
            pre = head
            head = next
        return pre


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.postorderTraversal(build([1, None, 2, 3])) == [3, 2, 1]
    assert sol.postorderTraversal(build([1, 2, 3, 4, 5])) == [4, 5, 2, 3, 1]
    assert sol.postorderTraversal(build([])) == []
    assert sol.postorderTraversal(build([1])) == [1]
