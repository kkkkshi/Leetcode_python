# 300. Longest Increasing Subsequence

# Dynamic programming
# Time: O(n^2)
# Space: O(n)
# 2023.06.21: no
# notes: dp[i] is the LIS ending at i, built from every smaller
#        earlier value
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


# Intelligently Build a Subsequence
# Time: O(n^2)
# Space: O(n)
# 2023.06.21: no
# notes: keep a candidate subsequence; append if bigger than the
#        last, else overwrite the first element it can replace, since
#        a smaller value leaves more room for later numbers
class Solution2:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num

        return len(sub)


# Improve With Binary Search
# Time: O(nlogn)
# Space: O(n)
# 2023.06.21: no
# notes: same as above but find the replace position with bisect
class Solution3:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)

            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num

        return len(sub)


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert sol.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert sol.lengthOfLIS([7, 7, 7, 7, 7]) == 1
    assert sol.lengthOfLIS([4, 10, 4, 3, 8, 9]) == 3
