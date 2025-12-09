# Line sweep
# Time: O(nlogn)
# Space: O(n)
# 2023.09.30: no
# notes: Line Sweep 第一次遇到，说一下解法，第一次看到肯定不会那种，但是思路气候司很简单
# 1. 考虑大顶点的面积和小顶点的面积是否相同
# 2. 判断是不是只有4个顶点，如果是偶数个节点，那就不是顶点，奇数个的才是顶点
# 3. 剩下的4个顶点也必须匹配大顶点的4个顶点
# 符合这3条的就可以构成一个长方形
# ps: labuladong讲的很好，链接：https://labuladong.github.io/algo/di-san-zha-24031/jing-dian--a94a0/ru-he-pan--6b2f8/
from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        X1, Y1 = float("inf"), float("inf")
        X2, Y2 = -float("inf"), -float("inf")

        points = set()
        actual_area = 0
        for x1, y1, x2, y2 in rectangles:
            # 计算完美矩形的理论顶点坐标
            X1, Y1 = min(X1, x1), min(Y1, y1)
            X2, Y2 = max(X2, x2), max(Y2, y2)
            # 累加小矩形的面积
            actual_area += (x2 - x1) * (y2 - y1)
            # 记录最终形成的图形中的顶点
            p1, p2 = (x1, y1), (x1, y2)
            p3, p4 = (x2, y1), (x2, y2)
            for p in [p1, p2, p3, p4]:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)
        # 判断面积是否相同
        expected_area = (X2 - X1) * (Y2 - Y1)
        if actual_area != expected_area:
            return False
        # 判断最终留下的顶点个数是否为 4
        if len(points) != 4:
            return False
        # 判断留下的 4 个顶点是否是完美矩形的顶点
        if (X1, Y1) not in points:
            return False
        if (X1, Y2) not in points:
            return False
        if (X2, Y1) not in points:
            return False
        if (X2, Y2) not in points:
            return False
        # 面积和顶点都对应，说明矩形符合题意
        return True


test = Solution()
test.isRectangleCover(
    [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
)
test.isRectangleCover([[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]])
test.isRectangleCover([[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]])
