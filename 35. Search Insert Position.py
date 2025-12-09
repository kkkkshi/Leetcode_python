# Find Lower bound Approach
# Time: O(logn)
# Space: O(1)
# 2024.06.04: yes
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo + hi)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                hi = mid-1
            else:
                lo = mid+1
        return lo

