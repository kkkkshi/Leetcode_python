# 33. Search in Rotated Sorted Array

# Binary Search Approach
# Time: O(logn)
# Space: O(1)
# 2023.06.25: yes
# notes: first binary search the rotation point (min), then pick the
#        sorted half that can contain target and binary search there
class Solution:

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                return mid+1
            elif nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[left]:
                right = mid
            else:
                return 0

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_value = self.findMin(nums)
        if target >= nums[min_value] and target <= nums[-1]:
            left, right = min_value, len(nums)-1
        else:
            left, right = 0, min_value-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid - 1
        if left < 0 or left >= len(nums):
            return -1
        return left if nums[left] == target else -1


# One Pass Binary Search Approach(best approach)
# Time: O(logn)
# Space: O(1)
# 2023.06.25: no
# notes: one binary search; at each step one half is sorted, decide
#        whether target lies in it and move accordingly
class Solution2:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 7) == 3
    assert sol.search([1], 0) == -1
    assert sol.search([1], 1) == 0
