# 283. Move Zeroes

# Approach (best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.08: yes
# notes: copy non-zero values forward, then fill the rest with zeros
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        fp, sp = 0, 0
        while fp < len(nums):
            if nums[fp] == 0:
                fp += 1
            else:
                nums[sp] = nums[fp]
                sp += 1
                fp += 1
        for i in range(sp, len(nums)):
            nums[i] = 0
        return nums


# Approach (best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.08: yes
# notes: mark the place we don't have non zero
class Solution2:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """
        lastNonZeroFoundAt = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[lastNonZeroFoundAt], nums[cur] = nums[cur], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1


# Tests:
for sol in (Solution(), Solution2()):
    a = [1, 2, 0, 3, 2, 0]
    sol.moveZeroes(a)
    assert a == [1, 2, 3, 2, 0, 0]
    b = [0, 0, 1]
    sol.moveZeroes(b)
    assert b == [1, 0, 0]
    c = [0]
    sol.moveZeroes(c)
    assert c == [0]
