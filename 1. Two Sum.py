# 1. Two Sum

# One-pass Hash Table Approach (best approach)
# Time: O(n)
# Space: O(n)
# 2023.06.23: yes
# notes: keep each number's index in a map; for each num, check if its
#        complement (target - num) was already seen
# skipped the brute force and two-pass hash table versions, not worth it
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results = {}
        for i in range(len(nums)):
            if target-nums[i] not in results:
                results[nums[i]] = i
            else:
                return [results[target-nums[i]], i]


# Tests:
for sol in (Solution(),):
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    assert sol.twoSum([3, 3], 6) == [0, 1]
