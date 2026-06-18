# 380. Insert Delete GetRandom O(1)

# HashMap + ArrayList Approach
# Time: O(1)
# Space: O(1)
# 2023.06.22: no
# notes: not familiar enough with data structures; the idea is easy
#        but the hashmap + arraylist combo is hard to come up with
import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.valToIndex = {}

    def insert(self, val):
        if val in self.valToIndex:
            return False
        self.valToIndex[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if val not in self.valToIndex:
            return False
        index = self.valToIndex[val]
        self.valToIndex[self.nums[-1]] = index
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        self.nums.pop()
        del self.valToIndex[val]
        return True

    def getRandom(self):
        return random.choice(self.nums)


# Tests:
obj = RandomizedSet()
assert obj.insert(1) is True
assert obj.insert(1) is False
assert obj.remove(2) is False
assert obj.insert(2) is True
assert obj.remove(1) is True
assert obj.getRandom() == 2
