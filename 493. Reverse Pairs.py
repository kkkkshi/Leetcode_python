# Merge sort Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.06.28: no
# notes: 更改merge，使左边排序好的每一个都对右边确认一下有几个两倍的
class Solution:
    def reversePairs(self, nums):
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

        end = mid + 1   # 左边比右边的大两倍的值，因为左边和右边都是sorted order, 左边的每一个值都需要像右边确认一遍是不是两倍
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


test = Solution()
test.reversePairs(nums = [4,10,2,5,1])
test.reversePairs([1,3,2,3,1])
