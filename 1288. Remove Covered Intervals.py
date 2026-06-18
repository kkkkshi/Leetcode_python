# 1288. Remove Covered Intervals

from typing import List


# Greedy
# Time: O(n)
# Space: O(n)
# 2023.09.11: yes
# notes: reviewed key = lambda x: (x[0], -x[1]); sort by start asc
#        and end desc, then count intervals whose end grows
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key = lambda x: (x[0], -x[1]))
        results = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][1] > results[-1][1]:
                results.append(intervals[i])
        return len(results)


# Tests:
for sol in (Solution(),):
    assert sol.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]) == 2
    assert sol.removeCoveredIntervals([[1, 4], [2, 3]]) == 1
    assert sol.removeCoveredIntervals([[3, 10], [4, 10], [5, 11]]) == 2
    assert sol.removeCoveredIntervals([[1, 2], [1, 4], [3, 4]]) == 1
