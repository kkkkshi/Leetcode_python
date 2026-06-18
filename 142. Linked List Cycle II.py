# 142. Linked List Cycle II

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def build(values, pos):
    # build a list; pos is the index the tail links back to, -1 for none
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1 and nodes:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


class Solution:
    # simple solution what I first thought
    # notes: record visited nodes; first repeat is the cycle entrance
    def detectCycle(self, head):
        visited = set()

        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None


class Solution2:
    # Floyd's Tortoise and Hare method
    # notes: find the meeting point, then walk one pointer from head and
    #        one from the meeting point; they meet at the entrance
    def getIntersect(self, head):
        tortoise = head
        hare = head

        # A fast pointer will either loop around a cycle and meet the slow
        # pointer or reach the `null` at the end of a non-cyclic list.
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return tortoise

        return None

    def detectCycle(self, head):
        if head is None:
            return None

        # If there is a cycle, the fast/slow pointers will intersect at some
        # node. Otherwise, there is no cycle, so we cannot find an entrance to
        # a cycle.
        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        # To find the entrance to the cycle, we have two pointers traverse at
        # the same speed -- one from the front of the list, and the other from
        # the point of intersection.
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1


class Solution3:
    # notes: same Floyd idea, fast starts two ahead and handles the
    #        no-cycle exits before resetting one pointer to head
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        p1, p2 = head.next.next, head.next
        if p1 == None:
            return None
        while p1 != p2:
            if p1 != None and p1.next != None:
                p1 = p1.next.next
                p2 = p2.next
            else:
                return None
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    head = build([3, 2, 0, -4], 1)
    assert sol.detectCycle(head).val == 2
    head = build([1, 2], 0)
    assert sol.detectCycle(head).val == 1
    assert sol.detectCycle(build([1], -1)) is None
    assert sol.detectCycle(None) is None
