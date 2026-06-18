# 973. K Closest Points to Origin

from random import randint
import heapq


# Sort
# Time: O(nlogn)
# Space: O(n)
# 2023.07.20: yes
# notes: sort all points by squared distance, take the first K
class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]


# Divide and Conquer
# Time: O(n)
# Space: O(n)
# 2023.07.20: no
# notes: we only need the top K, so quickselect-partition the array
#        and stop early; no full sort needed
class Solution2:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return

            # Put random element as A[i] - this is the pivot
            k = randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points) - 1, K)
        return points[:K]


# Heap
# Time: O(nlogn)
# Space: O(n)
# 2023.07.20: yes
# notes: push (distance, point) into a heap, pop the K smallest
class Solution3:
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def distance(x, y):
            return (x**2 + y**2)**0.5

        saving = []

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            result = distance(x, y)
            saving.append([result, [x,y]])
        heapq.heapify(saving)

        final = []
        for j in range(k):
            final.append(heapq.heappop(saving)[1])
        return final


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    res = sol.kClosest([[1, 3], [-2, 2]], 1)
    assert sorted(map(list, res)) == [[-2, 2]]
    res = sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
    assert sorted(map(list, res)) == [[-2, 4], [3, 3]]
    res = sol.kClosest([[0, 1], [1, 0]], 2)
    assert sorted(map(list, res)) == [[0, 1], [1, 0]]
