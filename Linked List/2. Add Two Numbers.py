# 2. Add Two Numbers

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(vals):
    head = ListNode(-1)
    cur = head
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return head.next


def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


# Linked Lists
# Time: O(n)
# Space: O(1)
# 2023.10.29: yes
# notes: add digit by digit, carry the 1 forward, then drain the
#        longer list and append a final carry if any
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        cur = head
        trading = 0
        while l1 and l2:
            if l1.val + l2.val + trading >= 10:
                    new_value = l1.val + l2.val + trading - 10
                    trading = 1
            else:
                new_value = l1.val + l2.val + trading
                trading = 0
            l1 = l1.next
            l2 = l2.next
            new_node = ListNode(new_value)
            cur.next = new_node
            cur = cur.next
        while l1:
            if l1.val + trading >= 10:
                trading = 1
                new_node = ListNode(l1.val + trading - 10)
            else:
                new_node = ListNode(l1.val + trading)
                trading = 0
            cur.next = new_node
            l1 = l1.next
            cur = cur.next
        while l2:
            if l2.val + trading >= 10:
                trading = 1
                new_node = ListNode(l2.val + trading - 10)
            else:
                new_node = ListNode(l2.val + trading)
                trading = 0
            cur.next = new_node
            l2 = l2.next
            cur = cur.next
        if trading == 1:
            new_node = ListNode(1)
            cur.next = new_node
        return head.next


# Tests:
for sol in (Solution(),):
    assert to_list(sol.addTwoNumbers(build([2, 4, 3]), build([5, 6, 4]))) == [7, 0, 8]
    assert to_list(sol.addTwoNumbers(build([0]), build([0]))) == [0]
    assert to_list(sol.addTwoNumbers(
        build([9, 9, 9, 9, 9, 9, 9]), build([9, 9, 9, 9]))) == [8, 9, 9, 9, 0, 0, 0, 1]
