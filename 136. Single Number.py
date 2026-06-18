# 136. Single Number

# Bit Manipulation
# Time: O(n)
# Space: O(1)
# 2023.08.02: yes
# notes: XOR everything; a^a = 0 and a^0 = a, so pairs cancel and the
#        lone number is left; other approaches are just arithmetic
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res


# Tests:
for sol in (Solution(),):
    assert sol.singleNumber([4, 1, 2, 1, 2]) == 4
    assert sol.singleNumber([2, 2, 1]) == 1
    assert sol.singleNumber([1]) == 1
