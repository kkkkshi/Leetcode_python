# 1295. Find Numbers with Even Number of Digits

# Array Approach
# Time: O(n)
# Space: O(1)
# notes: count numbers whose digit length is even by checking
#        the string length of each number
class Solution:
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(1 for num in nums if len(str(num)) % 2 == 0)


# Tests:
for sol in (Solution(),):
    assert sol.findNumbers([12, 345, 2, 6, 7896]) == 2
    assert sol.findNumbers([555, 901, 482, 1771]) == 1
    assert sol.findNumbers([1, 22, 333, 4444]) == 2
    assert sol.findNumbers([]) == 0
