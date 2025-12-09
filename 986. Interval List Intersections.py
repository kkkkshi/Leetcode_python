# Array
# Time: O(n)
# Space: O(n)
# 2023.09.12: yes
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
            else:
                print("emmm?")
        return results


# Greedy
# Time: O(n)
# Space: O(n)
# 2023.09.12: no
# notes: 很不错的方法，每次只比较一个，每次取max, min 根据lo <= hi可以判断是不是空的，就可以进行下一步了
# 虽然时间复杂度差不多，但是很不错
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
test = Solution()
test.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]])
test.intervalIntersection(firstList = [[1,3],[5,9]], secondList = [])