# Linked Lists
# Time: O(n)
# Space: O(1)
# 2023.10.29: yes

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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

# Test:
test = Solution()
l4 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l5 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
l6 = test.addTwoNumbers(l4,l5)

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
l3 = test.addTwoNumbers(l1, l2)

