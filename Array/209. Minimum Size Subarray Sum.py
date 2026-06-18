# 209. Minimum Size Subarray Sum

from typing import List


# Sliding Window
# Time: O(n)
# Space: O(1)
# 2023.06.11: yes
# notes: grow the window to the right adding to the sum; while the
#        sum reaches target, record length and shrink from the left
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_length = float('inf')
        left, right = 0, 0
        total = 0
        while right < len(nums):
            total += nums[right]
            while total >= target:
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return min_length if min_length != float("inf") else 0


# Tests:
for sol in (Solution(),):
    assert sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert sol.minSubArrayLen(4, [1, 4, 4]) == 1
    assert sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
