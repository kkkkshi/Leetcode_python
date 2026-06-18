# 128. Longest Consecutive Sequence

# HashSet and Intelligent Sequence Building Approach (best solution)
# Time: O(n)
# Space: O(n)
# 2023.06.23: no
# notes: the problem wants O(n), so sorting is off the table (though
#        it would still pass); only start counting from a number
#        that has no left neighbor in the set
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


# Tests:
for sol in (Solution(),):
    assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert sol.longestConsecutive([]) == 0
    assert sol.longestConsecutive([1, 2, 0, 1]) == 3
