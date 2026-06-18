# 328. Odd Even Linked List

# Two Pointers
# Time: O(mlogm) for sorting
# Space: O(n)
# 2023.07.06: yes
# notes: split nodes into an odd-index list and an even-index list by
#        position, then stitch the even list after the odd list
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(values):
    dummy = cur = ListNode(-1)
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 0
        odd_head = odd_cur = ListNode(-1)
        even_head = even_cur =  ListNode(-1)
        while head:
            if i % 2 == 0:
                odd_cur.next = head
                odd_cur = odd_cur.next
            else:
                even_cur.next = head
                even_cur = even_cur.next
            i += 1
            head = head.next
        odd_cur.next = even_head.next
        even_cur.next = None
        return odd_head.next


# Tests:
for sol in (Solution(),):
    assert to_list(sol.oddEvenList(build([1, 2, 3, 4, 5]))) == [1, 3, 5, 2, 4]
    assert to_list(sol.oddEvenList(
        build([2, 1, 3, 5, 6, 4, 7]))) == [2, 3, 6, 7, 1, 5, 4]
    assert to_list(sol.oddEvenList(build([]))) == []
    assert to_list(sol.oddEvenList(build([1]))) == [1]
