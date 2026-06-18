# 268. Missing Number

# Bit Manipulation
# Time: O(n)
# Space: O(1)
# 2023.08.02: yes
# notes: XOR all indexes, values and n; pairs cancel out and the
#        leftover is the missing number
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        res ^= len(nums)
        return res


# Sum up
# Time: O(n)
# Space: O(1)
# 2023.08.02: yes
# notes: the missing number is the expected 0..n sum minus the
#        actual sum of nums
class Solution2:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.missingNumber([3,0,1]) == 2
    assert sol.missingNumber([0,1]) == 2
    assert sol.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
    assert sol.missingNumber([0]) == 1
