# 528. Random Pick with Weight

import random


# Prefix Sums with Binary Search Approach
# Time: construction: O(n), pickIndex: O(logn)
# Space: construction: O(n), pickIndex: O(1)
# 2023.06.21: no
# notes: build prefix sums, draw a target in [1, total], then binary
#        search for the first prefix >= target
class Solution:
    def __init__(self, w):
        n = len(w)
        self.preSum = [0] * (n + 1)
        self.rand = random.Random()
        for i in range(1, n+1):
            self.preSum[i] = self.preSum[i - 1] + w[i - 1]

    def pickIndex(self):
        n = len(self.preSum)
        target = self.rand.randint(1, self.preSum[n - 1])
        return self.left_bound(self.preSum, target) - 1

    def left_bound(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid-1
            elif nums[mid] < target:
                left = mid +1
        return left


# Prefix Sums with Linear Search Approach
# Time: construction: O(n), pickIndex: O(n)
# Space: construction: O(n), pickIndex: O(1)
# 2023.06.21: no
# notes: build prefix sums, scale a random in [0, total), then scan
#        for the first prefix above it
class Solution2:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i


# Tests:
for cls in (Solution, Solution2):
    # single weight always returns index 0
    obj = cls([1])
    assert all(obj.pickIndex() == 0 for _ in range(20))
    # zero-weight indices are never picked, all picks stay in range
    obj = cls([0, 5, 0])
    picks = [obj.pickIndex() for _ in range(200)]
    assert all(p == 1 for p in picks)
    obj = cls([1, 3])
    assert all(p in (0, 1) for p in (obj.pickIndex() for _ in range(50)))
