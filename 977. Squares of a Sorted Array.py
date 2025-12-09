# Two pointers
# Time: O(n)
# Space: O(n)
# 2024.06.09: yes
# notes: 注意.insert()是O(n)，容易超时，不要随便用
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
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
class Solution2(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)