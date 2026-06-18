# 303. Range Sum Query - Immutable

# Caching Approach (best approach):
# Time: O(n)
# Space: O(1)
# 2023.06.19: yes
# notes: store prefix sums so a range sum is one subtraction
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sum_nums = [0]
        for i in range(len(nums)):
            self.sum_nums.append(self.sum_nums[i] + nums[i])

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.sum_nums[right+1] - self.sum_nums[left]


# Tests:
obj = NumArray([-2, 0, 3, -5, 2, -1])
assert obj.sumRange(0, 2) == 1
assert obj.sumRange(2, 5) == -1
assert obj.sumRange(0, 5) == -3
