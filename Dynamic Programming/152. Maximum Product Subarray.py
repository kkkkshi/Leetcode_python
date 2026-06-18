# 152. Maximum Product Subarray

# Dynamic Programming (actually brute force)
# Time: O(n^2)
# Space: O(n)
# 2023.07.31: yes
# notes: looks like dp but is really brute force, O(n^2):
#        product of every subarray [i, j]
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float("-inf")
        num_len = len(nums)
        dp = [[0 for _ in range(num_len)] for _ in range(num_len)]
        for i in range(num_len):
            dp[i][i] = nums[i]
            res = max(res, dp[i][i])
        for i in range(num_len):
            for j in range(i+1, num_len):
                dp[i][j] = dp[i][j-1]* nums[j]
                res = max(res, dp[i][j])
        return res


# Dynamic Programming (actually brute force)
# Time: O(n^2)
# Space: O(n)
# 2023.07.31: yes
# notes: real dp: track max and min product ending here, since a
#        negative number can swap them
class Solution2:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            max_so_far = temp_max
            result = max(max_so_far, result)
        return result


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.maxProduct([-2]) == -2
    assert sol.maxProduct([2, 3, -2, 4]) == 6
    assert sol.maxProduct([-2, 0, -1]) == 0
