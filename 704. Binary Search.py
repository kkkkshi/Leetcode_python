# 704. Binary Search

# Find the Exact Value Approach
# Time: O(logn)
# Space: O(1)
# 2024.06.03: yes
# notes: standard binary search on a sorted array; return the index
#        when nums[mid] equals target, else narrow the half
from bisect import bisect_right


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right: # <= is because right = len(nums) -1 , is closed interval
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid +1
            elif nums[mid] > target:
                right = mid-1
        return -1


# Find Lower bound Approach
# Time: O(logn)
# Space: O(1)
# 2023.06.21: no
# notes: the key is handling the ending and the boundary cases
class Solution2:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid-1
            elif nums[mid] < target:
                left = mid +1
        if left < 0 or left >= len(nums):
            return -1
        return left if nums[left] == target else -1


# Find Upper bound Approach
# Time: O(logn)
# Space: O(1)
# 2023.06.21: no
# notes: search for the upper bound, then right = left - 1 points
#        to the last matching element
class Solution3:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left + right) //2
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] <= target:
                left = mid +1
        # right = left -1
        if right < 0 or right >= len(nums):
            return -1
        return right if nums[right] == target else -1


# Use built-in tools Approach
# Time: O(logn)
# Space: O(1)
# 2023.06.21: no
# notes: bisect_right gives the insert point; the slot before it is
#        the target if it matches
class Solution4:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        idx = bisect_right(nums, target)
        if idx > 0 and nums[idx - 1] == target:
            return idx - 1
        else:
            return -1


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.search([-1,0,3,5,9,12], 9) == 4
    assert sol.search([-1,0,3,5,9,12], 2) == -1
    assert sol.search([5], 5) == 0
    assert sol.search([5], -5) == -1
