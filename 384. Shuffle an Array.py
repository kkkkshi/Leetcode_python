# 384. Shuffle an Array

# Fisher-Yates Algorithm
# Time: O(n)
# Space: O(n)
# 2023.08.04: no
# notes: Fisher-Yates, aka the shuffle algorithm: first slot has n
#        choices, second n-1, and so on, giving n! outcomes, so correct
import random


class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.rand = random.Random()

    def reset(self):
        return self.nums

    # shuffle algorithm
    def shuffle(self):
        n = len(self.nums)
        copy = self.nums.copy()
        for i in range(n):
            # generate a random number in [i, n-1]
            r = i + self.rand.randint(0, n - i - 1)
            # swap nums[i] and nums[r]
            copy[i], copy[r] = copy[r], copy[i]
        return copy


# Backtracking
# Time: O(n^2)
# Space: O(n)
# 2023.08.04: no
# notes: pick a random number from the array into a new array,
#        placing them one by one yields a random order
class Solution2:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        aux = list(self.array)

        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx)

        return self.array


# Tests:
for cls in (Solution, Solution2):
    obj = cls([1, 2, 3])
    assert obj.reset() == [1, 2, 3]
    assert sorted(obj.shuffle()) == [1, 2, 3]
    assert obj.reset() == [1, 2, 3]
