# 53. Maximum Subarray

import math


# Sliding Window
# Time: O(n)
# Space: O(1)
# 2023.07.24: no
# notes: grow the window; once the window sum drops below 0, shrink
#        from the left until it is positive, updating max as we go
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        windowsum, maxsum = 0, float("-inf")
        while right < len(nums):
            windowsum += nums[right]
            right += 1
            if windowsum > maxsum:
                maxsum = windowsum
            while windowsum < 0:
                windowsum -= nums[left]
                left += 1
        return maxsum


# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.24: no
# notes: dp[i] is the best sum ending at i: either start fresh at
#        nums[i] or extend dp[i-1]; take the max
class Solution2:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [nums[0]]
        for i in range(1,n):
            # maximum that end with nums[i]
            dp.append(max(dp[i-1]+nums[i], nums[i]))
        return max(dp)


# Dynamic Programming
# Time: O(n)
# Space: O(1)
# 2023.07.24: no
# notes: each dp value only needs dp[i-1], so collapse it to O(1)
class Solution3:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp_0 = nums[0]
        dp_1, res = 0, dp_0
        for i in range(1,n):
            # maximum that end with nums[i]
            dp_1 = max(nums[i], nums[i]+dp_0)
            dp_0 = dp_1
            res = max(res,dp_0)
        return res


# Brute Force
# Time: O(n^2)
# Space: O(1)
# notes: try every subarray; not recommended
class Solution4:
    # brute force, not recommended
    def maxSubArray(self, nums):
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        return max_subarray


# Prefix Sum
# Time: O(n)
# Space: O(1)
# 2023.07.24: no
# notes: presum holds the running total; the best subarray ending at i
#        is presum[i+1] - min(presum[0..i]), tracked as we go
class Solution5:
    # solve with the prefix sum trick
    def maxSubArray(self, nums):
        n = len(nums)
        preSum = [0] * (n + 1)
        preSum[0] = 0
        # build the prefix sum array of nums
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        res = float('-inf')
        minVal = float('inf')
        for i in range(n):
            # keep minVal as the minimum of preSum[0..i]
            minVal = min(minVal, preSum[i])
            # best subarray ending at nums[i] is preSum[i+1] - min(preSum[0..i])
            res = max(res, preSum[i + 1] - minVal)
        return res


# Divide and Conquer (Advanced)
# Time: O(nlogn)
# Space: O(logn)
# 2023.07.24: no
# notes: combine best-left, best-right, and the best span crossing the
#        middle (which must include mid-1 and mid+1) at each split
class Solution6:
    def maxSubArray(self, nums):
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)

        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)


# Kadane's Algorithm
# Time: O(n)
# Space: O(1)
# notes: keep a running sum; drop it when it goes negative, else extend
class Solution7:
    def maxSubArray(self, nums):
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]

        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4(),
            Solution5(), Solution6(), Solution7()):
    assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert sol.maxSubArray([-3, -4, -1, -5]) == -1
