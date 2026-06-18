# 239. Sliding Window Maximum

from collections import deque
from typing import List


# Monotonic Stack Approach (best approach)
# Time: O(n)
# Space: O(n)
# 2023.07.15: yes
# notes: keep a decreasing deque of indices; pop smaller values from
#        the back, drop out-of-window indices from the front, the front
#        is the window max
class Solution:
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


# Monotonic Stack Approach (best approach)
# Time: O(n)
# Space: O(n)
# 2023.09.10: yes
# notes: same idea storing (index, value) pairs; no need to track n
#        since the value comes along, and the index makes bounds checks
#        easier
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
for sol in (Solution(), Solution2()):
    assert sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert sol.maxSlidingWindow([1], 1) == [1]
    assert sol.maxSlidingWindow([1,-1], 1) == [1,-1]
    assert sol.maxSlidingWindow([9,8,7,6], 2) == [9,8,7]
