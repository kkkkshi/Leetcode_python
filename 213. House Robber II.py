# 213. House Robber II

# Iteration DP
# Time: O(n)
# Space: O(n)
# 2023.07.28: yes
# notes: houses form a circle, so the first and last can't both be
#        robbed; run linear robber on [0..n-2] and [1..n-1], take max
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        # dp1 -> 1 to n-1
        # dp2 -> 2 to n
        dp1 = [0] * n
        dp2 = [0] * n
        # if we have robbed the first house, then we can't rob the second house
        dp1[0] = nums[0]
        dp1[1] = nums[0]
        # if we didn't rob the first house, we will definitely rob the second
        dp2[0] = 0
        dp2[1] = nums[1]
        for i in range(2, n):
            # make the optimal choice at each house
            dp1[i] = max(nums[i] + dp1[i-2], dp1[i-1])
            dp2[i] = max(nums[i] + dp2[i-2], dp2[i-1])
        # dp1 is for nums[1 - (n-1)] so we won't consider the last house in this case
        # dp1[n-2] will be the max profit
        # and dp2 is for nums[2 - n] so we can take the last house
        return max(dp1[n-2], dp2[n-1])


# Recursion DP
# Time: O(n)
# Space: O(1)
# 2023.07.28: yes
# notes: same idea, compressed to O(1) space
class Solution2:
    def rob(self, nums):
        if len(nums) == 0 or nums is None:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums):
        t1 = 0
        t2 = 0
        for current in nums:
            temp = t1
            t1 = max(current + t2, t1)
            t2 = temp
        return t1


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.rob([2, 3, 2]) == 3
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([1, 2, 3]) == 3
    assert sol.rob([0]) == 0
    assert sol.rob([200, 3, 140, 20, 10]) == 340
