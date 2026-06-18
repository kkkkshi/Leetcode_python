# 1356. Sort Integers by The Number of 1 Bits

# Array Approach
# Time: O(1)
# Space: O(1)
# 2023.07.18: yes
# notes: sort by (popcount, value) so ties fall back to the number
import heapq


class Solution:
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr, key = lambda num : (sum((num >> i) & 1 for i in range(32)), num))


# Heap Approach
# Time: O(n log n)
# Space: O(n)
# 2023.07.18: yes
# notes: push (ones, num) into a heap, then pop them out in order
class Solution2:
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []
        for num in arr:
            ones = self.countBits(num)
            res.append((ones, num))
        heapq.heapify(res)
        finalres = []
        while len(res) > 0:
            finalres.append(heapq.heappop(res)[1])
        return finalres

    def countBits(self, n):
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.sortByBits([0,1,2,3,4,5,6,7,8]) == [0, 1, 2, 4, 8, 3, 5, 6, 7]
    assert sol.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]) == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    assert sol.sortByBits([2,3,5,7,11,13,17,19]) == [2, 3, 5, 17, 7, 11, 13, 19]
