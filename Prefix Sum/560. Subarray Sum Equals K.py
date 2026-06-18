# 560. Subarray Sum Equals K

# Prefix Sum with Hashmap
# Time: O(n)
# Space: O(n)
# notes: keep prefix-sum counts; for each prefix add how many times
#        prefix-k was seen, that many subarrays end here
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=0
        prefsum=0
        d={0:1}
        for num in nums:
            prefsum = prefsum + num
            if prefsum-k in d:
                ans = ans + d[prefsum-k]
            if prefsum not in d:
                d[prefsum] = 1
            else:
                d[prefsum] = d[prefsum]+1
        return ans


# Tests:
for sol in (Solution(),):
    assert sol.subarraySum([1, 1, 1], 2) == 2
    assert sol.subarraySum([1, 2, 3], 3) == 2
    assert sol.subarraySum([1], 0) == 0
    assert sol.subarraySum([-1, -1, 1], 0) == 1
