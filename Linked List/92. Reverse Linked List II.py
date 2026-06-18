# 92. Reverse Linked List II

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
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


# Two Recursive Approach:
# Time: O(n)
# Space: O(n)
# 2023.09.10: no
# notes: reverse the first right nodes once left reaches 1; reverseN
#        records the successor (node after the reversed part) and
#        reconnects the reversed head to it
# see https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-8f30d/di-gui-mo--10b77/
# 1. you must know how to reverse a linked list with recursion for this
# 2. reverseBetween walks down to the left node to start reversing
# 3. reverseN with n==1 records the node after the reversed part so we
#    can reattach it via head.next = successor; if not called from
#    reverseBetween, successor defaults to None as the head has no prev
# 4. the rest of reverseN is a normal reverse
class Solution:
    successor = None
    # reverse the previous N elements
    def reverseN(self, head, n):
        global successor
        if n == 1:
            successor = head.next
            return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = successor
        return last

    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head


# Recursive Approach:
# Time: O(n)
# Space: O(n)  # recursion pushes onto the stack, so O(n)
# 2023.09.10: no
# notes: don't change links, swap values instead; walk right forward
#        and left forward, then on the way back swap left/right values
#        and stop once the pointers meet or cross the midpoint
class Solution2:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop
            if n == 1:
                return
            right = right.next
            if m > 1:
                left = left.next
            recurseAndReverse(right, m - 1, n - 1)
            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True
            if not stop:
                left.val, right.val = right.val, left.val
                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next
        recurseAndReverse(right, m, n)
        return head


# Iterative Link Reversal Approach (best approach):
# Time: O(n)
# Space: O(1)
# 2023.06.18: no
# notes: walk to the start of the reversed range, remember its head and
#        the node before it, reverse the links step by step, then
#        reconnect the head and tail of the reversed segment
class Solution3:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head


# Tests:
# 1 2 3 4 5 -> 1 4 3 2 5
for sol in (Solution(), Solution2(), Solution3()):
    assert to_list(sol.reverseBetween(build([1, 2, 3, 4, 5]), 2, 4)) == [1, 4, 3, 2, 5]
    assert to_list(sol.reverseBetween(build([5, 4]), 1, 2)) == [4, 5]
    assert to_list(sol.reverseBetween(build([5]), 1, 1)) == [5]
