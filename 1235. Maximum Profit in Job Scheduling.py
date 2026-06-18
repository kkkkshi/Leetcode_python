# 1235. Maximum Profit in Job Scheduling

from bisect import bisect_left
import heapq


# Top-Down Dynamic Programming + Binary Search Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.06.26: no
# notes: sort jobs, binary search the next non-overlapping job, and
#        use top-down dp to decide whether to take the current job
class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = []
        memo = [-1] * (len(profit) + 1)

        for i in range(len(profit)):
            jobs.append([startTime[i], endTime[i], profit[i]])

        jobs.sort()
        start = [job[0] for job in jobs]

        def findMaxProfit(position):
            if position == len(profit):
                return 0
            if memo[position] != -1:
                return memo[position]

            nextIndex = bisect_left(start, jobs[position][1])

            maxProfit = max(findMaxProfit(position + 1),
                            jobs[position][2] + findMaxProfit(nextIndex))

            memo[position] = maxProfit
            return maxProfit

        return findMaxProfit(0)


# Bottom-Up Dynamic Programming + Binary Search Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.06.26: no
# notes: same idea but go right to left, keeping the best profit
#        reachable from each job as you move left
class Solution2:
    def findMaxProfit(self, startTime, jobs):
        length = len(startTime)
        memo = [0] * (length + 1)

        for position in range(length - 1, -1, -1):
            currProfit = 0

            nextIndex = bisect_left(startTime, jobs[position][1])

            if nextIndex != length:
                currProfit = jobs[position][2] + memo[nextIndex]
            else:
                currProfit = jobs[position][2]

            if position == length - 1:
                memo[position] = currProfit
            else:
                memo[position] = max(currProfit, memo[position + 1])

        return memo[0]

    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = []

        for i in range(len(profit)):
            jobs.append([startTime[i], endTime[i], profit[i]])

        jobs.sort()

        startTime = [job[0] for job in jobs]

        return self.findMaxProfit(startTime, jobs)


# Sorting + Priority Queue Approach (best approach)
# Time: O(nlogn)
# Space: O(n)
# 2023.06.26: no
# notes: a min-heap keyed by end time carries the best profit
#        available up to each start; pop finished jobs, then push
#        the current job with the running max profit added
class Solution3:
    def findMaxProfit(self, jobs):
        n = len(jobs)
        maxProfit = 0
        pq = []  # min heap having [endTime, profit]

        for i in range(n):
            start, end, profit = jobs[i][0], jobs[i][1], jobs[i][2]

            # keep popping while the heap is not empty and
            # jobs are not conflicting
            # update the value of maxProfit
            while pq and start >= pq[0][0]:
                maxProfit = max(maxProfit, pq[0][1])
                heapq.heappop(pq)

            # push the job with combined profit
            # if no non-conflicting job is present maxProfit will be 0
            heapq.heappush(pq, [end, profit + maxProfit])

        # update the value of maxProfit by comparing with
        # profit of jobs that exist in the heap
        while pq:
            maxProfit = max(maxProfit, pq[0][1])
            heapq.heappop(pq)

        return maxProfit

    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = []

        for i in range(len(profit)):
            jobs.append([startTime[i], endTime[i], profit[i]])

        jobs.sort()
        return self.findMaxProfit(jobs)


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]) == 120
    assert sol.jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]) == 150
    assert sol.jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]) == 6
