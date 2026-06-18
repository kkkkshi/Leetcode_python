# 1011. Capacity To Ship Packages Within D Days

# Binary Search Approach
# Time: O(nlogm), n is len(pile), m is maximum banana in a single pile
# Space: O(1)
# 2023.06.22: no
# notes: binary search on the capacity; watch the left/right bounds, the
#        comparison signs, and how the feasibility function f is written.
class Solution:
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        # left is at least one box per trip
        # right is shipping everything at once, i.e. the total sum
        left, right = 0, 0
        for w in weights:
            left = max(left, w)
            right += w

        while left <= right:
            mid = left + (right - left) // 2
            if self.f(weights, mid) <= days:
                right = mid -1
            else:
                left = mid + 1
        return left

    def f(self, weights, capacity):
        days = 0
        pos = 0
        while pos < len(weights):
            cap = capacity
            while pos < len(weights):
                if cap < weights[pos]:
                    break
                else:
                    cap -= weights[pos]
                    pos += 1
            days += 1
        return days


# Tests:
for sol in (Solution(),):
    assert sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5) == 15
    assert sol.shipWithinDays([3,2,2,4,1,4], 3) == 6
    assert sol.shipWithinDays([1,2,3,1,1], 4) == 3
