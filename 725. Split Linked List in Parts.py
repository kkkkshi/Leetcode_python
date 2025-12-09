# Split Input List (best approach)
# Time: O(n+k)
# Space: O(k)
# 2023.09.10: yes


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional, List


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
class Solution2(object):
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
a = ListNode(1, ListNode(2, ListNode(3)))
b = ListNode(
    1,
    ListNode(
        2,
        ListNode(
            3,
            ListNode(
                4,
                ListNode(
                    5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10)))))
                ),
            ),
        ),
    ),
)
test = Solution()
c = test.splitListToParts(a, 5)
d = test.splitListToParts(b, 3)
