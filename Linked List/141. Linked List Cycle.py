# 141. Linked List Cycle

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


# Hash Table
# Time: O(n)
# Space: O(n)
# 2023.09.03: yes
# notes: store visited nodes; a node seen twice means there is a cycle
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False


# Floyd's Cycle Finding Algorithm (best)
# Time: O(n)
# Space: O(1)
# 2023.09.03: yes
# notes: fast/slow pointers; they meet inside a cycle
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


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.hasCycle(build([3, 2, 0, -4], 1)) is True
    assert sol.hasCycle(build([1, 2], 0)) is True
    assert sol.hasCycle(build([1], -1)) is False
    assert sol.hasCycle(build([], -1)) is False
