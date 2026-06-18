# 382. Linked List Random Node

# Fisher-Yates Algorithm
# Time: O(n)
# Space: O(n)
# 2023.08.04: no
# notes: reservoir sampling; the math is unintuitive, skip the proof
import random


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


class Solution:
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self):
        r = random.Random()
        i = 0
        res = 0
        p = self.head
        # iterate over the linked list
        while p != None:
            i = i + 1
            # generate an integer in [0, i)
            # the chance it equals 0 is 1/i
            if 0 == r.randint(0, i - 1):
                res = p.val
            p = p.next
        return res

    # reference solution
    def getRandom2(self):
        """
        Returns a random node's value.
        """
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            # decide whether to include the element in reservoir
            if random.random() < 1 / scope:
                chosen_value = curr.val
            # move on to the next node
            curr = curr.next
            scope += 1
        return chosen_value


# Tests:
obj = Solution(build([7]))
assert obj.getRandom() == 7
assert obj.getRandom2() == 7

obj = Solution(build([1, 2, 3]))
assert obj.getRandom() in (1, 2, 3)
assert obj.getRandom2() in (1, 2, 3)
