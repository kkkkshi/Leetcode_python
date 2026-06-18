# 31. Next Permutation

# Single Pass Approach
# Time: O(n)
# Space: O(1)
# 2023.09.12: yes
# notes: scan from the right to find the first ascending pair, then
#        swap that pivot with the next larger value to its right and
#        reverse the suffix; if none is found the array is fully
#        descending, so just reverse the whole array
# brute force is n! permutations, skipped
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
for sol in (Solution(),):
    nums = [1, 2, 3]
    sol.nextPermutation(nums)
    assert nums == [1, 3, 2]

    nums = [3, 2, 1]
    sol.nextPermutation(nums)
    assert nums == [1, 2, 3]

    nums = [1, 1, 5]
    sol.nextPermutation(nums)
    assert nums == [1, 5, 1]

    nums = [1, 3, 2]
    sol.nextPermutation(nums)
    assert nums == [2, 1, 3]
