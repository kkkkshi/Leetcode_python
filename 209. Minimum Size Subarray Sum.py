# Sliding Window
# Time: O(n)
# Space: O(1)
# 2023.06.11: yes
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        left, right = 0, 0
        total = 0
        while right < len(nums):
            total += nums[right]
            while total >= target:
                min_length = min(min_length, right - left)
                total -= nums[left]
                left += 1
            right += 1
        return min_length if min_length != float("inf") else 0

