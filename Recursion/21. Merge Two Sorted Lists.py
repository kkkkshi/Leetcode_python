# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
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


# Iterative Approach
# Time: O(n+m)
# Space: O(1)
# notes: walk both lists, always splice the smaller head onto the
#        result, then attach whatever tail is left over
class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(-1)
        cur = dummy_head
        while list1 and list2:
            if list1.val >= list2.val:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
            else:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return dummy_head.next


# Tests:
for sol in (Solution(),):
    assert to_list(sol.mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(sol.mergeTwoLists(build([]), build([]))) == []
    assert to_list(sol.mergeTwoLists(build([]), build([0]))) == [0]
