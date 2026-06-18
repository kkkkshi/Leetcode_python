# 27. Remove Element

# Two Pointers Approach
# Time: O(n)
# Space: O(1)
# 2024.06.07: yes
# notes: fast pointer scans; whenever a value is not val, copy it to
#        the slow pointer and advance it; slow ends as the new length
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        sp = fp = 0
        while fp < len(nums):
            if nums[fp] == val:
                fp += 1
            else:
                nums[sp] = nums[fp]
                sp += 1
                fp += 1
        return sp


# Two Pointers - when elements to remove are rare
# Time: O(n)
# Space: O(1)
# 2023.06.07: no
# notes: swap a matching element with the last one to cut element
#        moves; same time and space, just a bit faster in practice
class Solution2:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                # Reduce array size by one
                n -= 1
            else:
                i += 1
        return n


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.removeElement([3,2,2,3], 3) == 2
    assert sol.removeElement([0,1,2,2,3,0,4,2], 2) == 5
    assert sol.removeElement([1], 1) == 0
    assert sol.removeElement([4,5], 6) == 2
