# 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
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


# Straight-Forward Approach
# Time: O(n)
# Space: O(1)
# 2023.06.18: yes
# notes: slow pointer holds the last kept node; advance the fast pointer
#        and relink only when it sees a new value
class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sp = fp = head
        while fp:
            if sp.val == fp.val:
                fp = fp.next
            else:
                sp.next = fp
                fp = fp.next
                sp = sp.next
        if sp:
            sp.next = None
        return head


# Tests:
for sol in (Solution(),):
    assert to_list(sol.deleteDuplicates(build([1,1,2]))) == [1,2]
    assert to_list(sol.deleteDuplicates(build([1,1,2,2,3,3]))) == [1,2,3]
    assert to_list(sol.deleteDuplicates(build([]))) == []
    assert to_list(sol.deleteDuplicates(build([1]))) == [1]
