# 589. N-ary Tree Preorder Traversal

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Recursion Approach
# Time: O(nlok)
# Space: O(logk)
# 2023.06.30: yes
# notes: visit the node, then recurse into each child in order
class Solution:
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def dfs(root):
            if root == None:
                return
            self.result.append(root.val)
            if root.children == None:
                return
            for child in root.children:
                dfs(child)
        self.result = []
        dfs(root)
        return self.result


# Iterations Approach
# Time: O(nlok)
# Space: O(logk)
# 2023.06.30: yes
# notes: stack-based, push children reversed so the first child is
#        popped first
class Solution2:
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
        return output


# Tests:
tree = Node(1, [Node(3, [Node(5, []), Node(6, [])]),
                Node(2, []), Node(4, [])])
for sol in (Solution(), Solution2()):
    assert sol.preorder(tree) == [1, 3, 5, 6, 2, 4]
    assert sol.preorder(Node(1, [])) == [1]
    assert sol.preorder(None) == []
