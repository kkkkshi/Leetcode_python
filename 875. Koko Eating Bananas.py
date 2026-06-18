# 875. Koko Eating Bananas

# Binary Search Approach
# Time: O(nlogm), n is len(pile), m is maximum banana in a single pile
# Space: O(1)
# 2023.06.21: no
# notes: binary search the eating speed; f(speed) gives the hours needed,
#        find the smallest speed that finishes within H hours.
import math


class Solution:
    def minEatingSpeed(self, piles, H):
        left = 1
        # right is a closed interval, so set it to the maximum value
        right = max(piles)

        # right is a closed interval, so use <= here
        while left <= right:
            mid = left + (right - left) // 2
            if self.f(piles, mid) <= H:
                # right is a closed interval, so use mid - 1
                right = mid - 1
            else:
                left = mid + 1
        return left

    def f(self, piles, x):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/x)
        return hours


# Tests:
for sol in (Solution(),):
    assert sol.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
