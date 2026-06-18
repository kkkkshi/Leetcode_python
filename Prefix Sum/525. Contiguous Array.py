# 525. Contiguous Array

# Prefix Count with Hashmap
# Time: O(n)
# Space: O(n)
# notes: treat 0 as -1, track the running count; equal 0s and 1s means
#        the same count repeats, so the span between them is balanced
class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_length = 0
        table = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index

        return max_length


# Tests:
for sol in (Solution(),):
    assert sol.findMaxLength([0, 1]) == 2
    assert sol.findMaxLength([0, 1, 0]) == 2
    assert sol.findMaxLength([0, 1, 0, 0, 1, 1, 0]) == 6
    assert sol.findMaxLength([1, 1, 1]) == 0
