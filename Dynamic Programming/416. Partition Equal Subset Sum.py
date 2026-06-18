# 416. Partition Equal Subset Sum

# Bottom Up Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: yes
# notes: target is half the total; subset-sum dp where dp[i][j] means
#        the first i numbers can reach sum j.
from functools import lru_cache


class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sumArray = sum(nums)
        if sumArray % 2 != 0:
            return False
        n = len(nums)
        sumArray //= 2
        dp = [[False] * (sumArray + 1) for _ in range(n + 1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n+1):
            for j in range(1, sumArray+1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    # once True it stays True
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i-1]]
        return dp[n][sumArray]


# Optimised Dynamic Programming - Using 1D Array
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: no
# notes: same dp rolled into one row, iterating j downward so each
#        number is used at most once.
class Solution2:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sumArray = sum(nums)
        if sumArray % 2 != 0:
            return False
        n = len(nums)
        sumArray //= 2
        dp = [False] * (sumArray + 1)
        dp[0] = True
        for i in range(n):
            for j in range(sumArray, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]
        return dp[sumArray]


# Top Down Dynamic Programming - Memoization
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: no
# notes: recurse choosing to take or skip each number, memoized on
#        (index, remaining target).
class Solution3:
    def canPartition(self, nums):
        @lru_cache(maxsize=None)
        def dfs(nums, n, subset_sum):
            # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
                    or dfs(nums, n - 1, subset_sum))
            return result
        # find sum of array elements
        total_sum = sum(nums)
        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(tuple(nums), n - 1, subset_sum)


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.canPartition([1, 5, 11, 5]) is True
    assert sol.canPartition([1, 2, 3, 5]) is False
    assert sol.canPartition([1, 1]) is True
    assert sol.canPartition([2, 2, 3, 5]) is False
