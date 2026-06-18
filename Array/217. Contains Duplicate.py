# 217. Contains Duplicate

# Sorting Approach
# Time: O(nlogn)
# Space: O(1)
# 2023.06.23: yes
# notes: sort, then any duplicate sits next to its equal neighbor
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True
        return False


# Hash Table Approach
# Time: O(n)
# Space: O(n)
# 2023.06.23: yes
# notes: track seen values in a set; a repeat means a duplicate
class Solution2:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        contains = set()
        for i in range(len(nums)):
            if nums[i] not in contains:
                contains.add(nums[i])
            else:
                return True
        return False


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.containsDuplicate([1, 2, 3, 1]) is True
    assert sol.containsDuplicate([1, 2, 3, 4]) is False
    assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert sol.containsDuplicate([1]) is False
