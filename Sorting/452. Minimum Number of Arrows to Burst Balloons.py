# 452. Minimum Number of Arrows to Burst Balloons

# Dynamic Programming
# Time: O(nlogn)
# Space: O(nlogn)
# 2023.07.29: yes
# notes: greedy; sort by end, shoot at the first end, and only add
#        an arrow when a balloon starts after that end
class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        # sort by x_end
        points.sort(key=lambda x: x[1])

        arrows = 1
        first_end = points[0][1]
        for x_start, x_end in points:
            # if the current balloon starts after the end of another one,
            # one needs one more arrow
            if first_end < x_start:
                arrows += 1
                first_end = x_end

        return arrows


# Tests:
for sol in (Solution(),):
    assert sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2
    assert sol.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) == 4
    assert sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) == 2
    assert sol.findMinArrowShots([]) == 0
