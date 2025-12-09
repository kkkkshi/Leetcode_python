# Single Pass Approach
# Time: O(n)
# Space: O(1)
# 2023.09.12: yes
# notes: 交换必须一个个交互，无语，方法是先确定正确顺序的那一个，然后从后往前遍历，确认比那一个大的数字，交互，再逆序排列后半部分
# 如果没有找到顺序的那一个，证明全部都是逆序，直接翻转整个array
# brute force是n!，不写了
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= nums[i+1]:
                for j in range(len(nums)-1, i, -1):
                    if nums[i] < nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i+1:] = nums[i+1:][::-1]
                        return
        nums[:] = nums[::-1]
        return

# Tests:
test = Solution()
test.nextPermutation([3,2,1])
test.nextPermutation([5,1,1])
test.nextPermutation([1,5,1])
test.nextPermutation([1,1,5])
test.nextPermutation([2,3,1])
test.nextPermutation([2,1,3])
test.nextPermutation([1,3,2])
test.nextPermutation([1,2,3])
