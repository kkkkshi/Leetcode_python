# 493. Reverse Pairs

# Merge sort Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.06.28: no
# notes: tweak the merge so each sorted left value checks how
#        many right values it is more than twice as large as
class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.count = 0
        self.sort(nums)
        return self.count

    def sort(self, nums):
        self.temp = [0] * len(nums)
        self._sort(nums, 0, len(nums) - 1)

    def _sort(self, nums, lo, hi):
        if lo == hi:
            return
        mid = lo + (hi - lo) // 2
        self._sort(nums, lo, mid)
        self._sort(nums, mid + 1, hi)
        self.merge(nums, lo, mid, hi)

    def merge(self, nums, lo, mid, hi):
        for i in range(lo, hi + 1):
            self.temp[i] = nums[i]

        end = mid + 1   # left is more than twice the right value; both halves are
                        # sorted, so each left value checks the right once
        for i in range(lo, mid + 1):
            while end <= hi and nums[i] > nums[end] * 2:
                end += 1
            self.count += end - (mid + 1)

        i, j = lo, mid + 1
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
    assert sol.reversePairs([4, 10, 2, 5, 1]) == 4
    assert sol.reversePairs([1, 3, 2, 3, 1]) == 2
    assert sol.reversePairs([2, 4, 3, 5, 1]) == 3
    assert sol.reversePairs([1]) == 0
