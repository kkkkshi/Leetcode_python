# 160. Intersection of Two Linked Lists

class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next


def build(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


# Hash Table Approach
# Time: O(m+n)
# Space: O(n)
# notes: this is what I thought of first; store every node of B in a
#        set, then walk A and return the first node already in it
class Solution:
    # hash table method, which is what I thought first
    def getIntersectionNode(self, headA, headB):
        nodes_in_B = set()

        while headB is not None:
            nodes_in_B.add(headB)
            headB = headB.next

        while headA is not None:
            # if we find the node pointed to by headA,
            # in our set containing nodes of B, then return the node
            if headA in nodes_in_B:
                return headA
            headA = headA.next
        return None


# Two Pointers Approach
# Time: O(m+n)
# Space: O(1)
# notes: walk both lists; when a pointer hits the end switch it to the
#        other head, so both meet at the intersection or at None
class Solution2:
    # important method
    def getIntersectionNode(self, headA, headB):
        p1 = headA
        p2 = headB
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA
        return p1


# Brute Force Approach
# Time: O(m*n)
# Space: O(1)
# notes: for each node in A, scan all of B looking for the same node
class Solution3:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        while headA is not None:
            pB = headB
            while pB is not None:
                if headA == pB:
                    return headA
                pB = pB.next
            headA = headA.next

        return None


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    # build a shared tail so the two lists intersect
    shared = build([8, 4, 5])
    a = ListNode(4, ListNode(1, shared))
    b = ListNode(5, ListNode(6, ListNode(1, shared)))
    assert sol.getIntersectionNode(a, b) is shared

    # no intersection
    a2 = build([2, 6, 4])
    b2 = build([1, 5])
    assert sol.getIntersectionNode(a2, b2) is None
