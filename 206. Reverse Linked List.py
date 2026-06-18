# 206. Reverse Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


# Iterative Approach (best approach):
# Time: O(n)
# Space: O(1)
# 2023.06.17: yes
# notes: walk the list flipping each next pointer to the prev node
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev


# Recursive Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.17: no
# notes: recurse to the last node, then point the next node back at
#        the current one and cut the old forward link
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


# Tests:
for sol in (Solution(), Solution2()):
    assert to_list(sol.reverseList(build([1, 2, 3]))) == [3, 2, 1]
    assert to_list(sol.reverseList(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(sol.reverseList(build([1]))) == [1]
    assert to_list(sol.reverseList(build([]))) == []
