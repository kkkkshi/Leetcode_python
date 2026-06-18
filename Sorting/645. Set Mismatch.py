# 645. Set Mismatch

# Recursion
# Time: O(n)
# Space: O(1)
# 2023.08.05: no
# notes: use each value as an index and flip that slot negative; a slot
#        already negative marks the duplicate, a still-positive slot
#        marks the missing number
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        dup = -1
        for i in range(n):
            # values are 1-based
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                dup = abs(nums[i])
            else:
                nums[index] *= -1

        missing = -1
        for i in range(n):
            if nums[i] > 0:
                # turn the index back into the value
                missing = i + 1

        return [dup, missing]


# Using XOR
# Time: O(n)
# Space: O(1)
# 2023.09.03: no
# notes: xor all values then all indices to get missing ^ repeated.
#        take its rightmost set bit, split numbers and indices into the
#        bit=1 and bit=0 groups, xor each group; the missing and the
#        repeated must land in different groups, then match by index
class Solution2:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        xor0 = 0
        xor1 = 0

        for n in nums:
            xor ^= n

        for i in range(1, len(nums) + 1):
            xor ^= i

        rightmostbit = xor & ~(xor - 1)

        for n in nums:
            if n & rightmostbit != 0:
                xor1 ^= n
            else:
                xor0 ^= n

        for i in range(1, len(nums) + 1):
            if i & rightmostbit != 0:
                xor1 ^= i
            else:
                xor0 ^= i

        for i in range(len(nums)):
            if nums[i] == xor0:
                return [xor0, xor1]

        return [xor1, xor0]


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.findErrorNums([1, 2, 2, 4]) == [2, 3]
    assert sol.findErrorNums([1, 1]) == [1, 2]
    assert sol.findErrorNums([2, 2]) == [2, 1]
    assert sol.findErrorNums([3, 2, 3, 4, 6, 5]) == [3, 1]
