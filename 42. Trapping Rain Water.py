# 42. Trapping Rain Water

# Dynamic Programming Approach
# Time: O(n)
# Space: O(n)
# 2023.07.19: no
# notes: scan from both sides, record the running max on each
#        side; water at i is min(left_max, right_max) - height[i]
from typing import List


class Solution:
    def trap(self, height):
        if not height:
            return 0

        ans = 0
        size = len(height)
        left_max = [0] * size
        right_max = [0] * size

        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max[size - 1] = height[size - 1]
        for i in range(size - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans


# Using 2 pointers Approach (best approach)
# Time: O(n)
# Space: O(1)
# 2023.07.19: no
# notes: walk inward from both ends; the lower side moves, and
#        the running max on each side updates only after it is
#        passed, so the global peak may never update
class Solution2:
    def trap(self, height):
        left = 0
        right = len(height) - 1
        ans = 0
        left_max = 0
        right_max = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1

        return ans


# stack Approach
# Time: O(n)
# Space: O(n)
# 2023.09.29: no
# notes: monotonic decreasing stack of indices; when a taller bar
#        appears, pop and add the water bounded between the new bar
#        and the bar below the popped one
class Solution3:
    def trap(self, height):
        ans = 0
        current = 0
        st = []

        while current < len(height):
            while st and height[current] > height[st[-1]]:
                top = st.pop()
                if not st:
                    break
                distance = current - st[-1] - 1
                bounded_height = min(height[current], height[st[-1]]) - height[top]
                ans += distance * bounded_height

            st.append(current)
            current += 1

        return ans


# Prefix max arrays Approach
# Time: O(n)
# Space: O(n)
# notes: same idea as the DP method but builds the left and right
#        running-max arrays explicitly, then sums the trapped water
class Solution4:
    def trap(self, height: List[int]) -> int:
        left_array, right_array = [], []
        left_max, right_max = 0,0
        for i in height:
            if i > left_max:
                left_max = i
            left_array.append(left_max)
        for j in height[::-1]:
            if j > right_max:
                right_max = j
            right_array.append(right_max)
        right_array = right_array[::-1]
        result = 0
        for k in range(len(height)):
            result += max(min(left_array[k], right_array[k]) - height[k], 0)
        return result


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert sol.trap([4,2,0,3,2,5]) == 9
    assert sol.trap([]) == 0
    assert sol.trap([1,2,3]) == 0
