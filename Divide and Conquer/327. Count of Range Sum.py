# 327. Count of Range Sum

# Merge sort Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.06.28: no
# notes: build prefix sums, then during merge sort use a sliding window
#        over the right half to count pairs whose difference lands in
#        [lower, upper]
class Solution:
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        self.lower = lower
        self.upper = upper
        preSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            preSum[i + 1] = nums[i] + preSum[i]
        self.count = 0
        self.sort(preSum)
        return self.count

    def sort(self, nums):
        self.temp = [0] * len(nums)
        self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, lo, hi):
        if lo == hi:
            return
        mid = lo + (hi - lo) // 2
        self.mergeSort(nums, lo, mid)
        self.mergeSort(nums, mid + 1, hi)
        self.merge(nums, lo, mid, hi)

    def merge(self, nums, lo, mid, hi):
        for i in range(lo, hi + 1):
            self.temp[i] = nums[i]

        start = mid + 1
        end = mid + 1
        for i in range(lo, mid + 1):
            while start <= hi and nums[start] - nums[i] < self.lower:
                start += 1
            while end <= hi and nums[end] - nums[i] <= self.upper:
                end += 1
            self.count += end - start

        i = lo
        j = mid + 1
        for p in range(lo, hi + 1):
            if i == mid + 1:
                nums[p] = self.temp[j]
                j += 1
            elif j == hi + 1:
                nums[p] = self.temp[i]
                i += 1
            elif self.temp[i] > self.temp[j]:
                nums[p] = self.temp[j]
                j += 1
            else:
                nums[p] = self.temp[i]
                i += 1


# Tests:
for sol in (Solution(),):
    assert sol.countRangeSum([-2, 5, -1], -2, 2) == 3
    assert sol.countRangeSum([0], 0, 0) == 1
    assert sol.countRangeSum([0, 0], 0, 0) == 3
    assert sol.countRangeSum([1, 2, 3], 10, 20) == 0
