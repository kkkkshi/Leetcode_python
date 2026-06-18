# 148. Sort List

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


# Top Down Merge Sort Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.07.05: no
# notes: split by the middle with two pointers, sort each half, merge
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(self, list1, list2):
        dummyHead = ListNode(0)
        ptr = dummyHead
        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
        if list1:
            ptr.next = list1
        else:
            ptr.next = list2
        return dummyHead.next

    def getMid(self, head):
        midPrev = None
        while head and head.next:
            if not midPrev:
                midPrev = head
            else:
                midPrev = midPrev.next
            head = head.next.next
        mid = midPrev.next
        midPrev.next = None
        return mid


# Bottom Up Merge Sort Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.07.05: no
# notes: merge runs of size 1, 2, 4, ... bottom up, doubling each pass
class Solution2:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        dummy = ListNode('s')
        dummy.next = head
        tmp = head
        length = 0
        while tmp:
            tmp = tmp.next
            length += 1
        step = 1
        while step < length:
            cur, tail = dummy.next, dummy
            while cur:
                left = cur
                right = self.split(left, step)
                cur = self.split(right, step)
                tail = self.merge2(left, right, tail)
            step <<= 1
        return dummy.next

    # merge 2 sorted lists, and append the result to head
    # return the tail
    def merge2(self, p1, p2, head):
        dummy = ListNode('#')
        p = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
                p = p.next
            else:
                p.next = p2
                p2 = p2.next
                p = p.next
        p.next = p1 or p2
        head.next = dummy.next
        while p.next: p = p.next
        return p

    # divide the linked list into two lists
    # first linked list contains n nodes
    # return the head of second linked list
    def split(self, head, n):
        for i in range(n - 1):
            if head:
                head = head.next
            else:
                break
        if not head: return None
        second = head.next
        head.next = None
        return second


# Tests:
for sol in (Solution(), Solution2()):
    assert to_list(sol.sortList(build([4, 2, 1, 3]))) == [1, 2, 3, 4]
    assert to_list(sol.sortList(build([-1, 5, 3, 4, 0]))) == [-1, 0, 3, 4, 5]
    assert to_list(sol.sortList(build([]))) == []
    assert to_list(sol.sortList(build([1]))) == [1]
