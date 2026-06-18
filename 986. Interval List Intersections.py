# 986. Interval List Intersections

# Array
# Time: O(n)
# Space: O(n)
# 2023.09.12: yes
# notes: two pointers; enumerate every overlap case explicitly and
#        advance the pointer whose interval ends first
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        results = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            if secondList[j][0] <= firstList[i][0] <= firstList[i][1] <= secondList[j][1]:
                results.append(firstList[i])
                i += 1
            elif secondList[j][0] <= firstList[i][0] <= secondList[j][1] <= firstList[i][1]:
                results.append([firstList[i][0], secondList[j][1]])
                j += 1
            elif firstList[i][0] <= secondList[j][0] <= secondList[j][1] <= firstList[i][1]:
                results.append(secondList[j])
                j += 1
            elif firstList[i][0] <= secondList[j][0] <= firstList[i][1] <= secondList[j][1]:
                results.append([secondList[j][0], firstList[i][1]])
                i += 1
            elif firstList[i][1] < secondList[j][0]:
                i += 1
            elif secondList[j][0] < firstList[i][1]:
                j += 1
        return results


# Greedy
# Time: O(n)
# Space: O(n)
# 2023.09.12: no
# notes: nice approach; take max of starts and min of ends, lo <= hi
#        means a real overlap, then drop the interval ending first
class Solution2:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.intervalIntersection(
        [[0, 2], [5, 10], [13, 23], [24, 25]],
        [[1, 5], [8, 12], [15, 24], [25, 26]],
    ) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    assert sol.intervalIntersection([[1, 3], [5, 9]], []) == []
    assert sol.intervalIntersection([], [[4, 8], [10, 12]]) == []
    assert sol.intervalIntersection([[1, 7]], [[3, 10]]) == [[3, 7]]
