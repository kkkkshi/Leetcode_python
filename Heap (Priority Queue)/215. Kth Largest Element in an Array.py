# 215. Kth Largest Element in an Array

import heapq
import random


# Min Heap Approach
# Time: O(nlok)
# Space: O(logk)
# 2023.06.30: yes
# notes: keep a min-heap of size k; its root is the kth largest
class Solution:
    def findKthLargest(self, nums, k):
        pq = []
        for e in nums:
            heapq.heappush(pq, e)
            if len(pq) > k:
                heapq.heappop(pq)
        return pq[0]


# Sort Approach
# Time: O(nlogn)
# Space: O(logn)
# 2023.06.30: yes
# notes: sort descending and take index k-1
class Solution2:
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]


# Quickselect Approach
# Time: O(n)
# Space: O(n)
# 2023.06.30: no
# notes: partition around a random pivot and recurse into the side
#        that holds the kth largest
class Solution3:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []
            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            if k <= len(left):
                return quick_select(left, k)
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            return pivot
        return quick_select(nums, k)


# Counting Sort Approach
# Time: O(n+m)
# Space: O(n)
# 2023.06.30: no
# notes: count occurrences by value, then scan from the top until
#        we have passed k elements
class Solution4:
    def findKthLargest(self, nums, k):
        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1

        remain = k
        for num in range(len(count) - 1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_value

        return -1


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert sol.findKthLargest([1], 1) == 1
    assert sol.findKthLargest([1, 5, 16, 12, 7, 55, 27], 4) == 12
