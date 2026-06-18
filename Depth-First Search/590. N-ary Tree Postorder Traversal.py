# 590. N-ary Tree Postorder Traversal


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Recursion Approach
# Time: O(nlok)
# Space: O(logk)
# 2023.06.30: yes
# notes: visit all children first, then append the node value
class Solution:
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def dfs(root):
            if root == None:
                return
            if root.children == None:
                self.result.append(root.val)
                return
            for child in root.children:
                dfs(child)
            self.result.append(root.val)
        self.result = []
        dfs(root)
        return self.result


# Iterations Approach
# Time: O(nlok)
# Space: O(logk)
# 2023.06.30: yes
# notes: preorder-style stack, push children left to right,
#        then reverse the output to get postorder
class Solution2:
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
            if root.children:
                for c in root.children:
                    stack.append(c)
        return output[::-1]


# Tests:
tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
for sol in (Solution(), Solution2()):
    assert sol.postorder(tree) == [5, 6, 3, 2, 4, 1]
    assert sol.postorder(None) == []
    assert sol.postorder(Node(1)) == [1]
