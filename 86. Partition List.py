# 86. Partition List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(vals):
    dummy = cur = ListNode(-1)
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


# Two Pointers Approach (best approach):
# Time: O(n)
# Space: O(1)
# 2023.06.17: yes
# notes: build two chains, one for values < x and one for >= x, keeping
#        the original order, then splice the small chain before the large.
class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_small = cur_small = ListNode(-1)
        dummy_large = cur_large = ListNode(-1)
        while head:
            if head.val >= x:
                cur_large.next = ListNode(head.val)
                cur_large = cur_large.next
            else:
                cur_small.next = ListNode(head.val)
                cur_small = cur_small.next
            head = head.next
        cur_small.next = dummy_large.next
        return dummy_small.next


# Tests:
for sol in (Solution(),):
    assert to_list(sol.partition(build([1, 4, 3, 2, 5, 2]), 3)) == [1, 2, 2, 4, 3, 5]
    assert to_list(sol.partition(build([2, 1]), 2)) == [1, 2]
    assert to_list(sol.partition(build([]), 3)) == []
