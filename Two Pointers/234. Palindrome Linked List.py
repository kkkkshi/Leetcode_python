# 234. Palindrome Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


# Copy into Array List and then Use Two Pointer Technique
# Time: O(n)
# Space: O(n)
# 2023.06.19: yes
# notes: copy values into a list and check it reads the same from both
#        ends
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        begin_pointer, end_pointer = 0, len(arr)-1
        while begin_pointer <= end_pointer:
            if arr[begin_pointer] == arr[end_pointer]:
                begin_pointer += 1
                end_pointer -= 1
            else:
                return False
        return True


# Reverse Second Half In-place(best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.19: yes
# notes: find the middle with fast/slow pointers, reverse the second
#        half, then compare it against the first half
class Solution2:
    def reverse(self, head):
        prev = None
        cur = head
        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp
        return prev

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fp = sp = head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        rev_head = self.reverse(sp)
        cur = head
        while rev_head:
            if rev_head.val == cur.val:
                rev_head = rev_head.next
                cur = cur.next
            else:
                return False
        return True


# Recursive Approach(advanced)
# Time: O(n)
# Space: O(n)
# 2023.06.19: no
# notes: postorder traversal of the list; the recursion compares the
#        tail-to-head order against a left pointer moving head-to-tail
class Solution3:
    left = None

    def isPalindrome(self, head):
        global left
        left = head
        return self.traverse(head)

    def traverse(self, right):
        global left
        if right is None:
            return True
        res = self.traverse(right.next)
        # postorder code, so this compares from the tail backwards
        res = res and (right.val == left.val)  # must carry the recursion result
        left = left.next # left moves forward, matching front against back
        return res


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.isPalindrome(build([1, 2, 2, 1])) is True
    assert sol.isPalindrome(build([1, 2, 3, 4])) is False
    assert sol.isPalindrome(build([1, 2, 1])) is True
    assert sol.isPalindrome(build([1])) is True
