# 703. Kth Largest Element in a Stream

# Array
# Time: O(n^2)
# Space: O(n)
# 2023.10.30: yes
# notes: keep the top k values sorted; add inserts in order and the
#        smallest of the k is the kth largest
import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.nums = nums
        self.k = k
        while len(self.nums) > self.k:
            self.nums.pop(0)

    def add(self, val: int) -> int:
        self.insert(val)
        return self.nums[0]

    def insert(self, val):
        if len(self.nums) >= self.k:
            if val > self.nums[0]:
                for i in range(len(self.nums)):
                    if val > self.nums[-1]:
                        self.nums.append(val)
                        break
                    if self.nums[i] >= val:
                        self.nums.insert(i, val)
                        break
                self.nums.pop(0)
        else:
            if len(self.nums) == 0:
                self.nums.append(val)
                return
            for i in range(len(self.nums)):
                if val > self.nums[-1]:
                    self.nums.append(val)
                    break
                if self.nums[i] >= val:
                    self.nums.insert(i, val)
                    break


# Heap
# Time: O(nlogn+mlogk)
# Space: O(n)
# 2023.10.30: no
# notes: keep a min-heap of size k; after each push pop the smallest so
#        the heap top is always the kth largest
class KthLargest2:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Tests:
for Impl in (KthLargest, KthLargest2):
    obj = Impl(3, [4, 5, 8, 2])
    assert obj.add(3) == 4
    assert obj.add(5) == 5
    assert obj.add(10) == 5
    assert obj.add(9) == 8
    assert obj.add(4) == 8

    obj = Impl(1, [])
    assert obj.add(-3) == -3
    assert obj.add(-2) == -2
    assert obj.add(-4) == -2
    assert obj.add(0) == 0
    assert obj.add(4) == 4
