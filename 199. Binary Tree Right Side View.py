# 199. Binary Tree Right Side View

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(vals):
    # build a tree from level-order values, None means missing
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


# breadth-first Search Approach (best approach)
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
# notes: BFS level by level; take the last node of each level
class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results = []
        if root == None:
            return results
        q = [root]
        while q:
            level_length = len(q)
            for i in range(level_length):
                node = q.pop(0)
                if i == level_length-1:
                    results.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return results


# depth-first Search Approach (beset approach)
# Time: O(n)
# Space: O(h), h is height
# 2023.07.03: yes
# notes: DFS visiting right before left; the first node seen at each
#        depth is the rightmost one
class Solution2:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        rightside = []

        def helper(node, level):
            if level == len(rightside):
                rightside.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)

        helper(root, 0)
        return rightside


# BFS: One Queue + Sentinel (not as clean as the first two)
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
# notes: one queue with a None sentinel marking level ends; the node
#        before each sentinel is the rightmost of its level
class Solution3:
    def rightSideView(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        queue = deque([root, None, ])
        rightside = []

        curr = root
        while queue:
            prev, curr = curr, queue.popleft()

            while curr:
                # add child nodes in the queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                prev, curr = curr, queue.popleft()

            # the current level is finished
            # and prev is its rightmost element
            rightside.append(prev.val)
            # add a sentinel to mark the end
            # of the next level
            if queue:
                queue.append(None)

        return rightside


# BFS: Two Queues (not as clean as the first three)
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
# notes: keep two queues, swap to the next level each round; the last
#        node popped from a level is the rightmost
class Solution4:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        next_level = deque([root, ])
        rightside = []

        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # The current level is finished.
            # Its last element is the rightmost one.
            rightside.append(node.val)

        return rightside


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.rightSideView(build([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert sol.rightSideView(build([1, None, 3])) == [1, 3]
    assert sol.rightSideView(build([])) == []
    assert sol.rightSideView(build([1, 2])) == [1, 2]
