# 337. House Robber III

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(values):
    """Build a binary tree from a level-order list (None = missing)."""
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


# Recursion
# Time: O(n)
# Space: O(n)
# 2023.07.28: yes
# notes: each node returns a tuple of (rob, not rob)
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            # return [rob this node, not rob this node]
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            # if we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            # else we could choose to either rob its children or not
            not_rob = max(left) + max(right)
            return [rob, not_rob]
        return max(helper(root))


# Recursion with Memoization
# Time: O(n)
# Space: O(n)
# 2023.07.28: yes
# notes: memoize by whether the parent was robbed; if parent was
#        robbed the children must not be robbed, otherwise each
#        child is free to take its own max
class Solution2:
    def rob(self, root):
        rob_saved = {}
        not_rob_saved = {}
        def helper(node, parent_robbed):
            if not node:
                return 0
            if parent_robbed:
                if node in rob_saved:
                    return rob_saved[node]
                result = helper(node.left, False) + helper(node.right, False)
                rob_saved[node] = result
                return result
            else:
                if node in not_rob_saved:
                    return not_rob_saved[node]
                rob = node.val + helper(node.left, True) + helper(node.right, True)
                not_rob = helper(node.left, False) + helper(node.right, False)
                result = max(rob, not_rob)
                not_rob_saved[node] = result
                return result
        return helper(root, False)


# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.28: yes
# notes: flatten the tree into arrays then run the same dp as the
#        recursion above, bottom up
class Solution3:
    def rob(self, root):
        if not root:
            return 0
        # reform tree into array-based tree
        tree = []
        graph = {-1: []}
        index = -1
        q = [(root, -1)]
        while q:
            node, parent_index = q.pop(0)
            if node:
                index += 1
                tree.append(node.val)
                graph[index] = []
                graph[parent_index].append(index)
                q.append((node.left, index))
                q.append((node.right, index))
        # represent the maximum start by node i with robbing i
        dp_rob = [0] * (index + 1)
        # represent the maximum start by node i without robbing i
        dp_not_rob = [0] * (index + 1)
        for i in reversed(range(index + 1)):
            if not graph[i]:  # if is leaf
                dp_rob[i] = tree[i]
                dp_not_rob[i] = 0
            else:
                dp_rob[i] = tree[i] + sum(dp_not_rob[child]
                                          for child in graph[i])
                dp_not_rob[i] = sum(max(dp_rob[child], dp_not_rob[child])
                                    for child in graph[i])
        return max(dp_rob[0], dp_not_rob[0])


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.rob(build([3, 2, 3, None, 3, None, 1])) == 7
    assert sol.rob(build([3, 4, 5, 1, 3, None, 1])) == 9
    assert sol.rob(build([])) == 0
    assert sol.rob(build([5])) == 5
