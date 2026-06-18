# 494. Target Sum

# Bottom Up Dynamic Programming
# Time: O(tn)
# Space: O(tn)
# 2023.07.25: no
# notes: dp[i][j] refers to the number of assignments which can lead to a sum of j up to the ith index
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        dp = [[0] * (2 * total + 1) for _ in range(len(nums))]
        dp[0][nums[0] + total] = 1
        dp[0][-nums[0] + total] += 1

        for i in range(1, len(nums)):
            for s in range(-total, total + 1):
                if dp[i - 1][s + total] > 0:
                    # the count never changes: there are only 2^n ways total, so this just
                    # carries dp[i-1][s+total] onto dp[i][s+nums[i]+total]; adding a number
                    # does not change the count, only merging paths does
                    dp[i][s + nums[i] + total] += dp[i - 1][s + total]
                    dp[i][s - nums[i] + total] += dp[i - 1][s + total]
        return 0 if abs(S) > total else dp[len(nums) - 1][S + total]


# Backtracking
# Time: O(2^n)
# Space: O(1)
# 2023.07.25: no
# notes: just one way to think about it; times out
class Solution2:
    def __init__(self):
        self.result = 0
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        self.backtrack(nums, 0, target)
        return self.result
    def backtrack(self, nums, i, remain):
        if i == len(nums):
            if remain == 0:
                self.result += 1
            return
        remain += nums[i]
        self.backtrack(nums, i + 1, remain)
        remain -= nums[i]
        remain -= nums[i]
        self.backtrack(nums, i + 1, remain)
        remain += nums[i]


# Recursion, non-standard answer
# Time: O(tn)
# Space: O(tn)
# 2023.07.25: no
# notes: use a string key for the memo
class Solution3:
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        memo = {}
        def dp(i, remain):
            # base case
            if i == len(nums):
                if remain == 0:
                    return 1
                return 0
            # turn the two into a string to use as a hash key
            key = str(i) + "," + str(remain)
            if key in memo:
                return memo[key]
            result = dp(i + 1, remain - nums[i]) + dp(i + 1, remain + nums[i])
            memo[key] = result
            return result
        return dp(0, target)


# Recursion, standard answer
# Time: O(tn)
# Space: O(tn)
# 2023.07.25: no
# notes: memo[i][sum + self.total] = add + subtract means the count returned on the add
#        branch plus the count on the subtract branch is the total count
class Solution4:
    def __init__(self):
        self.total = 0

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.total = sum(nums)
        memo = [[float('-inf')] * (2 * self.total + 1) for _ in range(len(nums))]
        return self.calculate(nums, 0, 0, S, memo)

    def calculate(self, nums, i, sum, S, memo):
        if i == len(nums):
            if sum == S:
                return 1
            else:
                return 0
        else:
            if memo[i][sum + self.total] != float('-inf'):
                return memo[i][sum + self.total]
            add = self.calculate(nums, i + 1, sum + nums[i], S, memo)
            subtract = self.calculate(nums, i + 1, sum - nums[i], S, memo)
            memo[i][sum + self.total] = add + subtract
            return memo[i][sum + self.total]


# 1D Dynamic Programming
# Time: O(tn)
# Space: O(t)
# 2023.07.25: no
# notes: same recursion with memo as solution4
class Solution5:
    def __init__(self):
        self.total = 0

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.total = sum(nums)
        memo = [[float('-inf')] * (2 * self.total + 1) for _ in range(len(nums))]
        return self.calculate(nums, 0, 0, S, memo)

    def calculate(self, nums, i, sum, S, memo):
        if i == len(nums):
            if sum == S:
                return 1
            else:
                return 0
        else:
            if memo[i][sum + self.total] != float('-inf'):
                return memo[i][sum + self.total]
            add = self.calculate(nums, i + 1, sum + nums[i], S, memo)
            subtract = self.calculate(nums, i + 1, sum - nums[i], S, memo)
            memo[i][sum + self.total] = add + subtract
            return memo[i][sum + self.total]


# Tests:
# Solution2/4/5 carry state, so build a fresh instance per assert.
for cls in (Solution, Solution2, Solution3, Solution4, Solution5):
    assert cls().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
    assert cls().findTargetSumWays([1, 0], 1) == 2
    assert cls().findTargetSumWays([1], 1) == 1
    assert cls().findTargetSumWays([1], 2) == 0
