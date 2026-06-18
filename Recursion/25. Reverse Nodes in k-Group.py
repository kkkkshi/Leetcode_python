# 25. Reverse Nodes in k-Group

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(values):
    # build a linked list from a python list
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head):
    # turn a linked list back into a python list
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


# Recursive Approach:
# Time: O(n)
# Space: O(n/k)
# 2023.06.19: no
# notes: the order is 206 -> 92 -> 25; lots of notes, details below
class Solution:
    # a plain recursion that reverses a linked list and returns the
    # new head (the old tail)
    def reverseLinkedList(self, head, k):

        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains
        # atleast k nodes.
        new_head, ptr = None, head
        while k:
            # Keep track of the next node to process in the
            # original list
            next_node = ptr.next

            # Insert the node pointed to by "ptr"
            # at the beginning of the reversed list
            ptr.next = new_head
            new_head = ptr

            # Move on to the next node
            ptr = next_node

            # Decrement the count of nodes to be reversed by 1
            k -= 1

        # Return the head of the reversed list
        return new_head

    def reverseKGroup(self, head, k):

        count = 0 # counter
        ptr = head

        # First, see if there are atleast k nodes
        # left in the linked list.
        while count < k and ptr:
            ptr = ptr.next
            count += 1

        # If we have k nodes, then we reverse them
        if count == k:
            # Reverse the first k nodes of the list and
            # get the reversed list's head.
            # just reverse this small linked list
            reversedHead = self.reverseLinkedList(head, k)

            # Now recurse on the remaining linked list. Since
            # our recursion returns the head of the overall processed
            # list, we use that and the "original" head of the "k" nodes
            # to re-wire the connections.
            # link the tail (the old head) to the reversed remainder;
            # key step, a classic one-liner
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        # if there are fewer than k nodes left, return the head as is
        # since nothing needs reversing
        return head


# Recursive Approach:
# Time: O(n)
# Space: O(n/k)
# 2023.06.19: no
# notes: labuladong's version, nicer than the standard one and easy
#        to follow; the trick is to stop at the node that does not
#        need reversing instead of stopping at None
class Solution3:
    # reverse the half-open range [a, b); note left-closed right-open
    def reverse(self, a, b):
        pre, cur, nxt = None, a, a
        # just change the stop condition of the while loop
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        # return the head after reversing
        return pre

    def reverseKGroup(self, head, k):
        if not head:
            return None
        # range [a, b) holds the k nodes to reverse
        a, b = head, head
        for i in range(k):
            # fewer than k nodes, no reversing needed, base case
            if not b:
                return head
            b = b.next
        # reverse the first k nodes, up to b
        new_head = self.reverse(a, b)
        # recurse on the rest and connect them
        a.next = self.reverseKGroup(b, k)
        return new_head


# Iterative O(1) space Approach:
# Time: O(n)
# Space: O(1)
# 2023.06.18: no
# notes: reverse each k-block in place and stitch blocks together
#        with ktail (previous block's tail) and head (next block)
class Solution2:

    def reverseLinkedList(self, head, k):

        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains
        # atleast k nodes.
        new_head, ptr = None, head
        while k:
            # Keep track of the next node to process in the
            # original list
            next_node = ptr.next

            # Insert the node pointed to by "ptr"
            # at the beginning of the reversed list
            ptr.next = new_head
            new_head = ptr

            # Move on to the next node
            ptr = next_node

            # Decrement the count of nodes to be reversed by 1
            k -= 1

        # Return the head of the reversed list
        return new_head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        ptr = head
        ktail = None

        # Head of the final, moified linked list
        new_head = None

        # Keep going until there are nodes in the list
        while ptr:
            count = 0

            # Start counting nodes from the head
            ptr = head

            # Find the head of the next k nodes
            while count < k and ptr:
                ptr = ptr.next
                count += 1

            # If we counted k nodes, reverse them
            if count == k:

                # Reverse k nodes and get the new head
                revHead = self.reverseLinkedList(head, k)

                # new_head is the head of the final linked list
                # this is the tail of the first reverse (no head yet);
                # afterwards new_head is set and this if is skipped
                if not new_head:
                    new_head = revHead

                # ktail is the tail of the previous block of
                # reversed k nodes
                # only the first assignment skips it, since the first
                # reverse has None before it; the rest enter, except
                # the final leftover which never reaches here
                if ktail:
                    ktail.next = revHead

                ktail = head
                head = ptr

        # attach the final, possibly un-reversed portion
        # the leftover that needs no reversing comes here, since head
        # is always the front and revHead is always the tail/new head
        if ktail:
            ktail.next = head

        return new_head if new_head else head


# Tests:
for sol in (Solution(), Solution3(), Solution2()):
    assert to_list(sol.reverseKGroup(build([1,2,3,4,5]), 2)) == [2,1,4,3,5]
    assert to_list(sol.reverseKGroup(build([1,2,3,4,5]), 3)) == [3,2,1,4,5]
    assert to_list(sol.reverseKGroup(build([1,2,3,4,5]), 1)) == [1,2,3,4,5]
    assert to_list(sol.reverseKGroup(build([1,2]), 2)) == [2,1]
