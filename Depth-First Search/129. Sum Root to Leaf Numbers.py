# 129. Sum Root to Leaf Numbers

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(values):
    # level-order build, None means missing node
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


# depth-first Search Approach
# Time: O(n)
# Space: O(n)
# 2023.07.03: yes
# notes: recurse down each path carrying the number built so far;
#        at a leaf add it to the running total
class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recursion(root, cur_value):
            if not root:
                return 0
            if root.left == None and root.right == None:
                self.total += cur_value*10+root.val
            recursion(root.left, cur_value*10 + root.val)
            recursion(root.right, cur_value*10 + root.val)
        self.total = 0
        recursion(root, 0)
        return self.total


# breadth-first Search Approach
# Time: O(n)
# Space: O(n)
# 2023.07.03: yes
# notes: walk the tree with a stack, building the number per node;
#        add it at each leaf
class Solution2:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        root_to_leaf = 0
        stack = [(root, 0)]

        while stack:
            root, curr_number = stack.pop()
            if root is not None:
                curr_number = curr_number * 10 + root.val
                # if it's a leaf, update root-to-leaf sum
                if root.left is None and root.right is None:
                    root_to_leaf += curr_number
                else:
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))

        return root_to_leaf


# Morris Approach
# Time: O(n)
# Space: O(1)
# 2023.07.03: no
# notes: thread predecessor links to traverse without a stack,
#        summing each leaf number as it is reached
class Solution3:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        root_to_leaf = curr_number = 0

        while root:
            # If there is a left child,
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left:
                # Predecessor node is one step to the left
                # and then to the right till you can.
                predecessor = root.left
                steps = 1
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                    steps += 1

                # Set link predecessor.right = root
                # and go to explore the left subtree
                if predecessor.right is None:
                    curr_number = curr_number * 10 + root.val
                    predecessor.right = root
                    root = root.left
                    # Break the link predecessor.right = root
                # Once the link is broken,
                # it's time to change subtree and go to the right
                else:
                    # If you're on the leaf, update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # This part of tree is explored, backtrack
                    for _ in range(steps):
                        curr_number //= 10
                    predecessor.right = None
                    root = root.right

                    # If there is no left child
            # then just go right.
            else:
                curr_number = curr_number * 10 + root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right

        return root_to_leaf

#     4
#   9   0
# 5 1


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.sumNumbers(build([1, 2, 3])) == 25
    assert sol.sumNumbers(build([4, 9, 0, 5, 1])) == 1026
    assert sol.sumNumbers(build([1])) == 1
