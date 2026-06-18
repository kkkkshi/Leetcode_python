# 35. Search Insert Position

# Find Lower bound Approach
# Time: O(logn)
# Space: O(1)
# 2024.06.04: yes
# notes: binary search; when target is missing, lo lands on the
#        first index where it should be inserted
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
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


# Tests:
for sol in (Solution(),):
    assert sol.searchInsert([1, 3, 5, 6], 5) == 2
    assert sol.searchInsert([1, 3, 5, 6], 2) == 1
    assert sol.searchInsert([1, 3, 5, 6], 7) == 4
    assert sol.searchInsert([1, 3, 5, 6], 0) == 0
