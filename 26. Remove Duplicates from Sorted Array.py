# 26. Remove Duplicates from Sorted Array

# Two indexes approach
# Time: O(n)
# Space: O(1)
# 2023.06.08: yes
# notes: slow pointer marks the last unique spot; fast pointer scans
#        ahead and copies a new value next to it when it differs
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sp = 0
        for fp in range(1, len(nums)):
            if nums[sp] != nums[fp]:
                sp += 1
                nums[sp] = nums[fp]
        return sp+1


# Two indexes approach
# Time: O(n)
# Space: O(1)
# notes: same idea written as an explicit while loop with two pointers
class Solution2:
    def removeDuplicates(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        sp, fp = 0, 1
        while fp < len(nums):
            if nums[sp] == nums[fp]:
                fp += 1
            else:
                sp += 1
                nums[sp] = nums[fp]
                fp += 1
        return sp+1


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.removeDuplicates([0,0,1,1,2,2,3,3,3]) == 4
    assert sol.removeDuplicates([1,2,2]) == 2
    assert sol.removeDuplicates([1]) == 1
    assert sol.removeDuplicates([1,1,1]) == 1
