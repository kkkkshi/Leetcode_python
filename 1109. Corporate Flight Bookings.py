# 1109. Corporate Flight Bookings

# Range Caching Approach (best approach):
# Time: O(1)
# Space: O(mn)
# 2023.06.19: yes
# notes: diff array - add inc at start, subtract after end, then the
#        prefix sum gives each flight's total seats
class Solution:
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        arr = [0] * n
        for booking in bookings:
            start, end, inc = booking
            arr[start-1] += inc
            if end < len(arr):
                arr[end] -= inc
        return_arr = [0]*n
        for i in range(len(arr)):
            return_arr[i] = return_arr[i-1] + arr[i]
        return return_arr


# Tests:
for sol in (Solution(),):
    assert sol.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5) == [10, 55, 45, 25, 25]
    assert sol.corpFlightBookings([[1,2,10],[2,2,15]], 2) == [10, 25]
    assert sol.corpFlightBookings([[1,1,5]], 1) == [5]
