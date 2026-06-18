# 725. Split Linked List in Parts

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(vals):
    head = cur = ListNode(0)
    for v in vals:
        cur.next = cur = ListNode(v)
    return head.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


# Split Input List (best approach)
# Time: O(n+k)
# Space: O(k)
# 2023.09.10: yes
# notes: count length, give each part length//k plus one extra to the
#        first length%k parts, then cut the links in place
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        length = 0
        cur = head
        results = []
        while cur:
            cur = cur.next
            length += 1
        num_element = length // k
        num_extra = length % k
        cur = head
        i = 0
        while cur:
            if i == 0:
                results.append(cur)
            i += 1
            tmp = cur
            cur = cur.next
            if i == num_element:
                if num_extra == 0:
                    i = 0
                    tmp.next = None
                else:
                    num_extra -= 1
            elif i > num_element:
                i = 0
                tmp.next = None
        while len(results) < k:
            results.append(None)
        return results


#  Create New Lists
# Time: O(n+k)
# Space: O(max(n, k))
# 2023.09.10: yes
# notes: copy values into k fresh lists, giving the first remainder
#        parts one extra node each
class Solution2:
    def splitListToParts(self, root, k):
        cur = root
        for N in range(1001):
            if not cur:
                break
            cur = cur.next
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in range(k):
            head = write = ListNode(None)
            for j in range(width + (i < remainder)):
                write.next = write = ListNode(cur.val)
                if cur:
                    cur = cur.next
            ans.append(head.next)
        return ans


# Tests:
for sol in (Solution(), Solution2()):
    parts = sol.splitListToParts(build([1, 2, 3]), 5)
    assert [to_list(p) for p in parts] == [[1], [2], [3], [], []]
    parts = sol.splitListToParts(build([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)
    assert [to_list(p) for p in parts] == [
        [1, 2, 3, 4], [5, 6, 7], [8, 9, 10]
    ]
    parts = sol.splitListToParts(build([1, 2, 3]), 1)
    assert [to_list(p) for p in parts] == [[1, 2, 3]]
