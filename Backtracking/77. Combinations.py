# 77. Combinations

# Backtracking
# Time: O(n!/((k-1)!(n-k)!))
# Space: O(n)
# 2023.08.02: yes
# notes: standard backtracking; the only extra rule is to record a
#        path once its length reaches k
class Solution:
    def combine(self, nums, k):
        """
        :type nums: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        track = []
        def backtrack(start, nums):
            if len(track) == k:
                res.append(list(track))
            for i in range(start, nums+1):
                track.append(i)
                backtrack(i+1, nums)
                track.pop()
        backtrack(1, nums)
        return res


# Tests:
for sol in (Solution(),):
    assert sol.combine(4, 2) == [
        [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]
    ]
    assert sol.combine(1, 1) == [[1]]
    assert sol.combine(5, 1) == [[1], [2], [3], [4], [5]]
