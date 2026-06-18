# 710. Random Pick with Blacklist

# Virtual Whitelist Approach (best approach)
# Time: O(1)
# Space: O(1)
# 2023.06.22: no
# notes: keep picks in [0, sz); map any blacklisted index in that
#        range to a non-blacklisted index from the tail
from typing import List
import random


class Solution:
    def __init__(self, N: int, blacklist: List[int]):
        # count of the valid numbers
        self.sz = N - len(blacklist)
        # record the blacklisted numbers in a hashmap
        self.mapping = {}
        for b in blacklist:
            self.mapping[b] = 666

        # remap blacklisted numbers to other positions
        last = N - 1
        for b in blacklist:
            if b >= self.sz:
                continue
            # find a position that is not mapped yet as the target
            while last in self.mapping:
                last -= 1
            # map b to last, and map the value at last to b
            self.mapping[b] = last
            last -= 1

    def pick(self) -> int:
        # pick a random index
        index = random.randint(0, self.sz - 1)
        # if the index is blacklisted, return its mapped value
        if index in self.mapping:
            return self.mapping[index]
        # otherwise return the index directly
        return index


# Binary Search over Blacklist Approach
# Time: O(blogb)
# Space: O(b)
# 2023.06.22: no
# notes: pick k in the whitelist count, binary search the blacklist
#        to shift k past the blacklisted numbers below it
import random


class Solution2:
    def __init__(self, N, blacklist):
        self.n = N
        blacklist.sort()
        self.b = blacklist

    def pick(self):
        k = random.randint(0, self.n - len(self.b) - 1)
        lo = 0
        hi = len(self.b) - 1

        while lo < hi:
            i = (lo + hi + 1) // 2
            if self.b[i] - i > k:
                hi = i - 1
            else:
                lo = i

        return k + lo + 1 if lo == hi and self.b[lo] - lo <= k else k


# Tests:
for Sol in (Solution, Solution2):
    obj = Sol(5, [2, 4])
    allowed = {0, 1, 3}
    for _ in range(50):
        assert obj.pick() in allowed
