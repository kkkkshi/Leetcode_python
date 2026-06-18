# 143. Reorder List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def build(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


# Reverse the Second Part of the List and Merge Two Sorted Lists Approach
# Time: O(n)
# Space: O(1)
# notes: cut in half, reverse the back half, then weave them together
class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        fp = sp = head
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
        prev, cur = None, sp
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        # curr.next, prev, curr = prev, curr, curr.next (smart)
        p1, p2 = head, prev
        while p2.next:
            p1.next, p1 = p2, p1.next
            p2.next, p2 = p1, p2.next


# Tests:
for sol in (Solution(),):
    h = build([1, 2, 3, 4])
    sol.reorderList(h)
    assert to_list(h) == [1, 4, 2, 3]
    h = build([1, 2, 3, 4, 5])
    sol.reorderList(h)
    assert to_list(h) == [1, 5, 2, 4, 3]
