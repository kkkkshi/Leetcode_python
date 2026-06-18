# 23. Merge k Sorted Lists

import heapq


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


def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


# Optimize Approach 2 by Priority Queue
# Time: O(n log k)
# Space: O(k)
# notes: push each list head into a heap keyed by value, pop the
#        smallest and push its next, until the heap is empty
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Since python3 will have some comparison bugs, I have to add these two lines for heapq comparison
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val

        dummy_head = ListNode(-1)  # create a dummy head
        cur = dummy_head
        h = []  # create the heapq
        for i in lists:
            # check for the list is an empty list or not
            if i:
                heapq.heappush(h, (i.val, i))
            # when the heapq still have some element in it, continue the loop
        while h:
            val, node = heapq.heappop(h)
            cur.next = node
            node = node.next
            cur = cur.next
            # check if the node reaches the end, and whether to put the new element in the heapq
            if node:
                heapq.heappush(h, (node.val, node))
            # return the results
        return dummy_head.next


# Merge with Divide And Conquer
# Time: O(n log k)
# Space: O(1)
# notes: repeatedly merge lists in pairs at growing intervals until a
#        single merged list remains
class Solution2:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next


# brute force, not recommended
# Time: O(n log n)
# Space: O(n)
# notes: collect every value, sort them, then rebuild one list
class Solution3:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    lists = [build([1, 4, 5]), build([1, 3, 4]), build([2, 6])]
    assert to_list(sol.mergeKLists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert to_list(sol.mergeKLists([])) == []
    assert to_list(sol.mergeKLists([build([])])) == []
    assert to_list(sol.mergeKLists([build([2]), build([1])])) == [1, 2]
