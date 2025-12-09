# Monotonic Stack Approach (best approach)
# Time: O(n)
# Space: O(n)
# 2023.07.15: yes
# notes: 构建一个单调栈从大到小，如果当前值和单调栈第一个一样，那就压出，后续往单调栈里压的时候，如果比最后一个值大，
# 就弹出最后一个值，直到当前值比最后一个值小才能压入，以此类推
from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()
        res = []
        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            if dq and dq[0] == i-k:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            res.append(nums[dq[0]])
        return res

from typing import List

# Monotonic Stack Approach (best approach)
# Time: O(n)
# Space: O(n)
# 2023.09.10: yes
# notes: update一下，根本就不需要记录n，只需要记录index即可，因为可以直接拿到数字，记录Index也会更容易对比有没有越界
# dq[0]就是第一个element, dp[-1]就是最后一个element
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        q = deque()
        for i, n in enumerate(nums):
            if len(q) == 0:
                q.append((i, n))
            else:
                while len(q) == 0 or q[-1][1] < n:
                    if len(q) == 0:
                        break
                    q.pop()
                q.append((i, n))
            if q[0][0] <= i-k:
                q.popleft()
            if i-k >= -1:
                results.append(q[0][1])
        return results

# Tests:
test = Solution2()
test.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)












