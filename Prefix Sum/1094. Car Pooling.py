# 1094. Car Pooling

# Time Stamp Approach:
# Time: O(nlogn)
# Space: O(n)
# 2023.06.19: yes
# notes: turn each trip into a +k pickup and -k drop event, sort by
#        time, sweep and check the running load never exceeds cap
class Solution2:
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[0]])

        timestamp.sort()

        used_capacity = 0
        for time, passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True


# Bucket Sort Approach:
# Time: O(n)
# Space: O(1)
# 2023.06.19: yes
# notes: locations are bounded, so use a diff array over the buckets
#        and sweep the prefix sum instead of sorting events
class Solution3:
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] -= trip[0]

        used_capacity = 0
        for passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True


# Difference Array Approach:
# Time: O(n)
# Space: O(1)
# 2023.06.19: yes
# notes: same diff array idea, building the prefix sum into a second
#        array and checking each value against capacity
class Solution:
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        diff_arr = [0] * 1001
        result_arr = [0] * 1001
        for trip in trips:
            passenger, start, end = trip
            diff_arr[start] += passenger
            if end < len(diff_arr):
                diff_arr[end] -= passenger
            for i in range(len(diff_arr)):
                result_arr[i] = result_arr[i-1] + diff_arr[i]
                if result_arr[i] > capacity:
                    return False
        return True


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.carPooling([[2,1,5],[3,3,7]], 4) is False
    assert sol.carPooling([[2,1,5],[3,3,7]], 5) is True
    assert sol.carPooling([[9,0,1],[3,3,7]], 4) is False
    assert sol.carPooling([[2,1,5],[3,5,7]], 3) is True
