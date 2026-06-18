# 287. Find the Duplicate Number

# Binary Search
# Time: O(nlogn)
# Space: O(1)
# 2023.10.29: yes
# notes: nums hold 1..n, so for a guess count how many are <= it; if
#        the count exceeds the guess the duplicate is in the low half
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1
        while low <= high:
            cur = (low + high) // 2
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
        return duplicate


# Sum of Set Bits
# Time: O(nlogn)
# Space: O(1)
# 2023.10.29: no
# notes: per bit, if it is set more often in nums than in 1..n the
#        duplicate must have that bit set
class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = 0
        n = len(nums) - 1
        bits = n.bit_length()
        for bit in range(bits):
            mask = 1 << bit
            base_count = 0
            nums_count = 0
            for i in range(n + 1):
                # If bit is set in number (i) then add 1 to base_count
                if i & mask:
                    base_count += 1

                # If bit is set in nums[i] then add 1 to nums_count
                if nums[i] & mask:
                    nums_count += 1

            # If the current bit is more frequently set in nums than it is in
            # the range [1, 2, ..., n] then it must also be set in the duplicate number.
            if nums_count - base_count > 0:
                duplicate |= mask

        return duplicate


# Floyd's algorithm (best approach)
# Time: O(nlogn)
# Space: O(1)
# 2023.10.29: yes
# notes: treat values as next-pointers; the cycle entry found by the
#        tortoise and hare is the duplicate value
class Solution3:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.findDuplicate([1, 3, 4, 2, 2]) == 2
    assert sol.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert sol.findDuplicate([1, 1]) == 1
    assert sol.findDuplicate([2, 2, 2, 2, 2]) == 2
