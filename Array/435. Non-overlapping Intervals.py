# 435. Non-overlapping Intervals

# Dynamic Programming
# Time: O(nlogn)
# Space: O(nlogn)
# 2023.07.29: yes
# notes: greedy, hard to think of; sort by end time, and if the
#        current start is before the previous end, remove it
class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        ans = 0
        k = float('-inf')
        for start, end in intervals:
            if start >= k:
                k = end
            else:
                ans += 1
        return ans


# Tests:
for sol in (Solution(),):
    assert sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
    assert sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
    assert sol.eraseOverlapIntervals([[1,2],[2,3]]) == 0
    assert sol.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]) == 2
