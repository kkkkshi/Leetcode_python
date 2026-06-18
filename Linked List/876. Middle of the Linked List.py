# 876. Middle of the Linked List

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


# Fast and Slow Pointer Approach (best approach):
# Time: O(n)
# Space: O(1)
# 2023.06.17: yes
# notes: fast moves two steps per slow step, so slow lands on the middle
#        when fast runs off the end; for even length pick the second one.
class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head = fp = sp = ListNode(-1)
        dummy_head.next = head
        while fp:
            if fp.next:
                fp = fp.next.next
                sp = sp.next
            else:
                break
        if not fp:
            return sp
        else:
            return sp.next


# Output to Array Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.17: yes
# notes: dump the nodes into an array and index the middle directly.
class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]


# Tests:
for sol in (Solution(), Solution2()):
    assert to_list(sol.middleNode(build([1, 2, 3, 4, 5]))) == [3, 4, 5]
    assert to_list(sol.middleNode(build([1, 2, 3, 4, 5, 6]))) == [4, 5, 6]
    assert to_list(sol.middleNode(build([1]))) == [1]
