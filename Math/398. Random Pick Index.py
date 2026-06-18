# 398. Random Pick Index

import random
from collections import defaultdict


# Brute Force
# Time: O(n)
# Space: O(n)
# 2023.08.04: no
# notes: scan for all indices equal to target, then pick one uniformly.
class Solution:
    def __init__(self, nums):
        # Do not allocate extra space for the nums array
        self.nums = nums
        self.rand = random.Random()

    def pick(self, target):
        indices = []
        n = len(self.nums)
        for i in range(n):
            if self.nums[i] == target:
                indices.append(i)
        l = len(indices)
        # pick an index at random
        random_index = indices[self.rand.randint(0, l - 1)]
        return random_index


# Caching results using a hashmap
# Time: O(n)
# Space: O(n)
# 2023.08.04: no
# notes: precompute target -> list of indices, then pick one uniformly.
class Solution2:
    def __init__(self, nums):
        self.rand = random.Random()
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target):
        l = len(self.indices[target])
        # pick an index at random
        random_index = self.indices[target][self.rand.randint(0, l - 1)]
        return random_index


# Reservoir sampling
# Time: O(n)
# Space: O(n)
# 2023.08.04: no
# notes: one pass; keep the i-th matching index with probability 1/count
#        so every match ends up equally likely.
class Solution3:
    def __init__(self, nums):
        self.nums = nums
        self.rand = random.Random()

    def pick(self, target):
        count = 0
        idx = 0
        for i, num in enumerate(self.nums):
            # if nums[i] is equal to target, i is a potential candidate
            # which needs to be chosen uniformly at random
            if num == target:
                # increment the count of total candidates
                # available to be chosen uniformly at random
                count += 1
                # we pick the current number with probability 1 / count (reservoir sampling)
                if self.rand.randint(1, count) == 1:
                    idx = i
        return idx


# Tests:
nums = [1, 2, 3, 3, 3]
for cls in (Solution, Solution2, Solution3):
    obj = cls(nums)
    assert obj.pick(1) == 0
    assert nums[obj.pick(3)] == 3
    assert obj.pick(3) in (2, 3, 4)
