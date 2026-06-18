# 377. Combination Sum IV

# Backtracking (times out)
# Time: O(2^n)
# Space: O(1)
# 2023.09.11: no
import functools
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def backtrack(cur_target):
            nonlocal results
            if cur_target == 0:
                results += 1
                return
            for num in nums:
                if cur_target - num >= 0:
                    backtrack(cur_target - num)

        results = 0
        backtrack(target)
        return results


# Top down DP
# Time: O(tn)
# Space: O(t)
# 2023.09.11: no
class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        @functools.lru_cache(maxsize=None)
        def backtrack(cur_target):
            if cur_target == 0:
                return 1
            result = 0
            for num in nums:
                if cur_target - num >= 0:
                    result += backtrack(cur_target - num)
            return result

        return backtrack(target)


# Bottom Up Dp
# Time: O(tn)
# Space: O(t)
# 2023.09.11: no
class Solution3:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            for j in nums:
                if i-j >= 0:
                    dp[i] += dp[i-j]
        return dp[target]


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.combinationSum4([1, 2, 3], 4) == 7
    assert sol.combinationSum4([9], 3) == 0
    assert sol.combinationSum4([3, 2, 1], 4) == 7
    assert sol.combinationSum4([2], 4) == 1
