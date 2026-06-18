# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


# One Pass Algorithm Approach (best approach):
# Time: O(l), l is the length of nodes
# Space: O(1)
# 2023.06.17: yes
# notes: advance a fast pointer n steps ahead, then move both until
#        fast hits the end so slow lands before the target
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_head = ListNode(-1)
        dummy_head.next = head
        fp = sp = dummy_head
        for i in range(n):
            fp = fp.next
        while fp.next:
            fp = fp.next
            sp = sp.next
        sp.next = sp.next.next
        return dummy_head.next


# Two Pass Algorithm Approach:
# Time: O(l), l is the length of nodes
# Space: O(1)
# 2023.06.17: yes
# notes: first pass counts the length, second pass walks to the node
#        before the target and unlinks it
class Solution2:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head
        while first is not None:
            length += 1
            first = first.next
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next


# Tests:
for sol in (Solution(), Solution2()):
    assert to_list(sol.removeNthFromEnd(build([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert to_list(sol.removeNthFromEnd(build([1]), 1)) == []
    assert to_list(sol.removeNthFromEnd(build([1, 2]), 1)) == [1]
    assert to_list(sol.removeNthFromEnd(build([1, 2]), 2)) == [2]
