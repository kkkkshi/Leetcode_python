# 354. Russian Doll Envelopes

from bisect import bisect_left


# Sort + Longest Increasing Subsequence
# Time: O(nlogn)
# Space: O(n)
# 2023.06.21: no
# notes: sort by width, then run LIS on the heights to get the answer
class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        return lis([i[1] for i in envelopes])


# Tests:
for sol in (Solution(),):
    assert sol.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3
    assert sol.maxEnvelopes([[1, 1], [1, 1], [1, 1]]) == 1
    assert sol.maxEnvelopes([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]) == 4
