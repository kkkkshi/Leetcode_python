# 391. Perfect Rectangle

# Line sweep
# Time: O(nlogn)
# Space: O(n)
# 2023.09.30: no
# notes: a perfect cover holds when total small-rect area equals the
#        bounding-box area and exactly 4 corner points remain unpaired,
#        and those 4 points are the bounding box corners.
# a point cancels out if it appears an even number of times, so only
# real corners survive.
# ps: labuladong explains it well, link:
# https://labuladong.github.io/algo/di-san-zha-24031/jing-dian--a94a0/ru-he-pan--6b2f8/
from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        X1, Y1 = float("inf"), float("inf")
        X2, Y2 = -float("inf"), -float("inf")

        points = set()
        actual_area = 0
        for x1, y1, x2, y2 in rectangles:
            # theoretical corners of the perfect rectangle
            X1, Y1 = min(X1, x1), min(Y1, y1)
            X2, Y2 = max(X2, x2), max(Y2, y2)
            # accumulate the area of the small rectangle
            actual_area += (x2 - x1) * (y2 - y1)
            # record the corners of the final figure
            p1, p2 = (x1, y1), (x1, y2)
            p3, p4 = (x2, y1), (x2, y2)
            for p in [p1, p2, p3, p4]:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)
        # check whether the areas match
        expected_area = (X2 - X1) * (Y2 - Y1)
        if actual_area != expected_area:
            return False
        # check whether exactly 4 corners remain
        if len(points) != 4:
            return False
        # check the 4 remaining corners are the perfect-rectangle corners
        if (X1, Y1) not in points:
            return False
        if (X1, Y2) not in points:
            return False
        if (X2, Y1) not in points:
            return False
        if (X2, Y2) not in points:
            return False
        # area and corners match, so the rectangle is valid
        return True


# Tests:
for sol in (Solution(),):
    assert sol.isRectangleCover(
        [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
    ) is True
    assert sol.isRectangleCover(
        [[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]
    ) is False
    assert sol.isRectangleCover(
        [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]]
    ) is False
