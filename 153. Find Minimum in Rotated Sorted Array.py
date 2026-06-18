# 153. Find Minimum in Rotated Sorted Array

# Binary Search Approach (best approach)
# Time: O(logn)
# Space: O(1)
# 2023.06.25: yes
# notes: the answer always exists; mind the boundary updates
#        left = mid and right = mid
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[left]:
                right = mid
            else:
                return nums[0]


# Tests:
for sol in (Solution(),):
    assert sol.findMin([3, 1, 2]) == 1
    assert sol.findMin([1]) == 1
    assert sol.findMin([11, 13, 15, 17]) == 11
    assert sol.findMin([3, 4, 5, 1, 2]) == 1
    assert sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
