# Two indexes approach
# Time: O(n)
# Space: O(1)
# 2023.06.08: yes
class Solution(object):
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

class Solution2:
    def removeDuplicates(self, nums) -> int:
        sp, fp = 0, 1
        while fp < len(nums):
            if nums[sp] == nums[fp]:
                fp += 1
            else:
                sp += 1
                nums[sp] = nums[fp]
                fp += 1
        return sp+1

# test
a = [0,0,1,1,2,2,3,3,3]
b = [1,2,2]
test = Solution2()
result = test.removeDuplicates(a)
result2 = test.removeDuplicates(b)


