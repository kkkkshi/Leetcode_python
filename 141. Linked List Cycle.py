# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

# Hash Table
# Time: O(n)
# Space: O(n)
# 2023.09.03: yes
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False

# Floyd's Cycle Finding Algorithm (最优解)
# Time: O(n)
# Space: O(1)
# 2023.09.03: yes
# notes: 快慢指针
class Solution2:
    def hasCycle(self, head):
        if not head:
            return False
        p1, p2 = head.next, head
        while p1 != p2:
            if not p1 or not p1.next:
                return False
            p1 = p1.next.next
            p2 = p2.next
        return True

a = ListNode(3, ListNode(1))
b = ListNode(2, a)
# a.next.next = b
test = Solution()
test.hasCycle(a)
