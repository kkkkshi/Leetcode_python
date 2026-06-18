# 252. Meeting Rooms

# Sorting
# Time: O(nlogn)
# Space: O(1)
# 2023.07.31: yes
# notes: sort by start time; if any meeting starts before the
#        previous one ends, they overlap
class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


# Tests:
for sol in (Solution(),):
    assert sol.canAttendMeetings([[7,10],[2,4]]) is True
    assert sol.canAttendMeetings([[0,30],[5,10],[15,20]]) is False
    assert sol.canAttendMeetings([]) is True
    assert sol.canAttendMeetings([[5,8],[6,8]]) is False
