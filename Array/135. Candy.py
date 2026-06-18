# 135. Candy

# BruteForce (TLE)
# Time: O(n^2)
# Space: O(n)
# 2023.09.13: no
from typing import List
# notes: repeatedly bump a child above a smaller neighbor and set
#        changed=True; stop once a full pass makes no change
class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = [1] * n
        has_changed = True

        while has_changed:
            has_changed = False
            for i in range(n):
                if (
                    i < n - 1
                    and ratings[i] > ratings[i + 1]
                    and candies[i] <= candies[i + 1]
                ):
                    candies[i] = candies[i + 1] + 1
                    has_changed = True
                if (
                    i > 0
                    and ratings[i] > ratings[i - 1]
                    and candies[i] <= candies[i - 1]
                ):
                    candies[i] = candies[i - 1] + 1
                    has_changed = True
        return sum(candies)


# Using two arrays
# Time: O(n)
# Space: O(n)
# 2023.09.13: no
# notes: one left-to-right pass and one right-to-left pass, each
#        adding 1 over a smaller neighbor, then take the max
class Solution2:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        sum = 0
        left2right = [1] * n
        right2left = [1] * n

        # Scan from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1

        # Scan from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right2left[i] = right2left[i + 1] + 1

        # Calculate the total number of candies
        for i in range(n):
            sum += max(left2right[i], right2left[i])

        return sum


# Using one arrays
# Time: O(n)
# Space: O(n)
# 2023.09.13: no
# notes: like above but reuse one array; tracking the rightmost
#        value saves a bit of space, helps a little
class Solution3:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = [1] * n
        # Scan from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        sum = candies[n - 1]
        # Scan from right to left and update candies
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
            sum += candies[i]
        return sum


# Single Pass Approach with Constant Space
# Time: O(n)
# Space: O(1)
# 2023.09.13: no
# notes: didn't fully get it; Solution5 has the O(1) way, parts of
#        this one are still unclear, will update later
class Solution4:
    def count(self, n):
        return (n * (n + 1)) // 2

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings) <= 1:
            return len(ratings)

        candies = 0
        up = 0
        down = 0
        old_slope = 0

        for i in range(1, len(ratings)):
            new_slope = (
                1
                if ratings[i] > ratings[i - 1]
                else (-1 if ratings[i] < ratings[i - 1] else 0)
            )

            if (old_slope > 0 and new_slope == 0) or (old_slope < 0 and new_slope >= 0):
                candies += self.count(up) + self.count(down) + max(up, down)
                up = 0
                down = 0

            if new_slope > 0:
                up += 1
            elif new_slope < 0:
                down += 1
            else:
                candies += 1

            old_slope = new_slope

        candies += self.count(up) + self.count(down) + max(up, down) + 1
        return candies


# Single Pass Approach with Constant Space
# Time: O(n)
# Space: O(1)
# 2023.09.13: no
# notes: decide each child's candy from its slope vs the previous.
# On a plain rise, just add how many steps up so far. If a rise
# follows a descent, it's a valley, so reset down,up = 0,1 to start
# fresh, since a 3,2,1 descent must end at 1 or you overpay; the new
# start is then 1+1 = 2.
# On a flat spot also reset down,up = 0,1, but here up only needs +1.
# On a descent like 4,3,2 you can hand out 1,2,3 by swapping, so just
# count how many steps down. When down >= up (only when a descent
# directly follows a flat) the start is 1+1 = 2, since the flat is 1
# and this child is lower.
class Solution5:
    def candy(self, ratings: List[int]) -> int:
        """
        :type ratings: List[int]
        :rtype: int
        """
        ans = down = up = 0
        for i in range(len(ratings)):
            if not i or ratings[i - 1] < ratings[i]:
                if down:
                    down, up = 0, 1
                up += 1
                ans += up
            elif ratings[i - 1] == ratings[i]:
                down, up = 0, 1
                ans += 1
            else:
                down += 1
                ans += down if down < up else down + 1
        return ans


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4(), Solution5()):
    assert sol.candy([1, 0, 2]) == 5
    assert sol.candy([1, 2, 2]) == 4
    assert sol.candy([1, 3, 2, 2, 1]) == 7
    assert sol.candy([1, 2, 3, 4, 5, 3, 2, 1, 2, 6, 5, 4, 3, 3, 2, 1, 1, 3, 3, 3, 4, 2]) == 47
