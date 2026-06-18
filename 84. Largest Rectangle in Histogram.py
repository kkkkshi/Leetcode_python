# 84. Largest Rectangle in Histogram

# Using Stack (best approach)
# Time: O(n)
# Space: O(n)
# 2023.07.20: no
# notes: keep a stack of indices with increasing heights; when a
#        shorter bar comes, pop and settle each popped bar's area
class Solution:
    def largestRectangleArea(self, heights):
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)
        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        return max_area


# Divide and Conquer
# Time: O(nlogn)
# Space: O(n^2)
# 2023.07.20: no
# notes: split at the lowest bar; the answer is the best of that bar
#        spanning the whole range or the best in the left/right parts
class Solution2:
    def largestRectangleArea(self, heights):
        def calculateArea(heights, start, end):
            if start > end:
                return 0
            min_index = start
            for i in range(start, end + 1):
                if heights[min_index] > heights[i]:
                    min_index = i
            return max(
                heights[min_index] * (end - start + 1),
                calculateArea(heights, start, min_index - 1),
                calculateArea(heights, min_index + 1, end),
            )
        return calculateArea(heights, 0, len(heights) - 1)


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert sol.largestRectangleArea([2, 4]) == 4
    assert sol.largestRectangleArea([0]) == 0
    assert sol.largestRectangleArea([1, 1, 1, 1]) == 4
