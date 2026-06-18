# 2534. Time Taken to Cross the Door

from collections import deque


# Queue
# Time: O(n)
# Space: O(1)
# 2023.08.18: yes
# notes: keep an enter queue and an exit queue; each second admit all
#        arrivals so far, then let one through favoring the prev side;
#        looks like a double loop but is O(n) overall
class Solution:
    def timeTaken(self, arrival, state):
        """
        :type arrival: List[int]
        :type state: List[int]
        :rtype: List[int]
        """
        enter_pool, exit_pool = deque(),deque()
        cur_time = 0
        prev_state = 1
        i = 0
        ans = [0 for _ in range(len(arrival))]
        while i < len(arrival) or enter_pool or exit_pool:
            while i < len(arrival) and arrival[i] <= cur_time:
                if state[i] == 0:
                    enter_pool.append(i)
                else:
                    exit_pool.append(i)
                i += 1
            if prev_state == 1:
                if exit_pool:
                    ans[exit_pool.popleft()] = cur_time
                elif enter_pool:
                    ans[enter_pool.popleft()] = cur_time
                    prev_state = 0
            else:
                if enter_pool:
                    ans[enter_pool.popleft()] = cur_time
                elif exit_pool:
                    ans[exit_pool.popleft()] = cur_time
                    prev_state = 1
                else:
                    prev_state = 1
            cur_time += 1
        return ans


# Tests:
for sol in (Solution(),):
    assert sol.timeTaken([0,1,1,2,4], [0,1,0,0,1]) == [0,3,1,2,4]
    assert sol.timeTaken([0,0,0], [1,0,1]) == [0,2,1]
    assert sol.timeTaken([5], [0]) == [5]
