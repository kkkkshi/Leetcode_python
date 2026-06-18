# 149. Max Points on a Line

# Math
# Time: O(n^2)
# Space: O(n)
# 2023.07.22: no
# notes: use arctan to get the angle between two points; points
#        sharing the same angle from i lie on one line
import collections
import math


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for i in range(n):
            cnt = collections.defaultdict(int)
            for j in range(n):
                if j != i:
                    cnt[math.atan2(points[j][1] - points[i][1],
                                   points[j][0] - points[i][0])] += 1
            result = max(result, max(cnt.values()) + 1)
        return result


# Tests:
for sol in (Solution(),):
    assert sol.maxPoints([[1, 1], [2, 2], [3, 3]]) == 3
    assert sol.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
    assert sol.maxPoints([[0, 0]]) == 1
