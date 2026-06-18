# 55. Jump Game

from enum import Enum


class Index(Enum):
    GOOD = 0
    BAD = 1
    UNKNOWN = 2


# Greedy
# Time: O(n)
# Space: O(1)
# 2023.07.29: yes
# notes: track the furthest reachable index in one pass; if some
#        index sits beyond it we can never get there
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_length = nums[0]
        n = len(nums)
        for i in range(n):
            if max_length < i:
                return False
            if nums[i] + i > max_length:
                max_length = nums[i] + i
        return max_length >= n-1


# Dynamic Programming Top-down
# Time: O(n^2)
# Space: O(n)
# 2023.07.29: no
# notes: too slow but worth knowing; from a point recurse to every
#        reachable point, mark good/bad along the way; we don't need
#        those points to still return the furthest distance
class Solution2:
    def canJumpFromPosition(self, position, nums, memo):
        if memo[position] != Index.UNKNOWN:
            return memo[position] == Index.GOOD

        furthest_jump = min(position + nums[position], len(nums) - 1)
        for next_position in range(position + 1, furthest_jump + 1):
            if self.canJumpFromPosition(next_position, nums, memo):
                memo[position] = Index.GOOD
                return True

        memo[position] = Index.BAD
        return False

    def canJump(self, nums):
        memo = [Index.UNKNOWN] * len(nums)
        memo[-1] = Index.GOOD
        return self.canJumpFromPosition(0, nums, memo)


# Dynamic Programming Top-down
# Time: O(n)
# Space: O(1)
# 2023.07.29: no
# notes: barely passes; the bottom-up dp form, working backwards
class Solution3:
    def canJump(self, nums):
        memo = [Index.UNKNOWN] * len(nums)
        memo[-1] = Index.GOOD

        for i in range(len(nums) - 2, -1, -1):
            furthest_jump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthest_jump + 1):
                if memo[j] == Index.GOOD:
                    memo[i] = Index.GOOD
                    break
        return memo[0] == Index.GOOD


# Backtracking
# Time: O(2^n)
# Space: O(n)
# 2023.07.29: no
# notes: 2^n, blows up when n is large
class Solution4:
    def canJumpFromPosition(self, position, nums):
        if position == len(nums) - 1:
            return True

        furthest_jump = min(position + nums[position], len(nums) - 1)
        for next_position in range(position + 1, furthest_jump + 1):
            if self.canJumpFromPosition(next_position, nums):
                return True

        return False

    def canJump(self, nums):
        return self.canJumpFromPosition(0, nums)


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.canJump([2, 3, 1, 1, 4]) is True
    assert sol.canJump([3, 2, 1, 0, 4]) is False
    assert sol.canJump([0]) is True
    assert sol.canJump([2, 0, 0]) is True
