# 485. Max Consecutive Ones

# One Pass Counting
# Time: O(n)
# Space: O(1)
# notes: count the current run of 1s; reset on 0 and track the
#        max seen so far
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # save the maxCount for comparison
        count = maxCount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxCount = max(maxCount,count)
            else:
                count = 0
        return max(maxCount, count)


# Tests:
for sol in (Solution(),):
    assert sol.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
    assert sol.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
    assert sol.findMaxConsecutiveOnes([0, 0, 0]) == 0
    assert sol.findMaxConsecutiveOnes([1, 1, 1]) == 3
