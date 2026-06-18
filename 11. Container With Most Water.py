# 11. Container With Most Water

# Two Pointer Algorithm (best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.24: no
# notes: two pointers, move the shorter side inward each step, since
#        going inward only helps when the new line is taller
# Sept 29 update: greedy view, to move inward pick the taller side so
#        the area has a chance to grow
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxarea


# Tests:
for sol in (Solution(),):
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert sol.maxArea([1, 1]) == 1
    assert sol.maxArea([4, 3, 2, 1, 4]) == 16
