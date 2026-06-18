# 977. Squares of a Sorted Array

from typing import List


# Two pointers
# Time: O(n)
# Space: O(n)
# 2024.06.09: yes
# notes: compare abs of both ends, fill result from the back; avoid
#        .insert() since it is O(n) and can time out
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        results = [0]*len(nums)
        position = len(nums)-1
        left, right = 0, len(nums)-1
        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                results[position] = nums[right] **2
                right -= 1
            else:
                results[position] = nums[left] **2
                left += 1
            position -= 1
        return results


# Sort
# Time: O(nlogn)
# Space: O(n)
# 2024.06.09: yes
# notes: square every element then sort
class Solution2:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(x*x for x in A)


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert sol.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    assert sol.sortedSquares([1, 2, 3]) == [1, 4, 9]
    assert sol.sortedSquares([-5]) == [25]
