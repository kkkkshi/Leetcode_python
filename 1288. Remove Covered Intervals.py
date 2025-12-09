# Greedy
# Time: O(n)
# Space: O(n)
# 2023.09.11: yes
# notes: 复习了一下key = lambda x: (x[0], -x[1])的东西
from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: (x[0], -x[1]))
        results = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][1] > results[-1][1]:
                results.append(intervals[i])
        return len(results)

# Tests:
test = Solution()
test.removeCoveredIntervals([[1,2],[1,4],[3,4]])
test.removeCoveredIntervals([[3,10],[4,10],[5,11]])
test.removeCoveredIntervals([[1,4],[3,6],[2,8]])
