# Array
# Time: O(n^2)
# Space: O(n)
# 2023.10.30: yes
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
# notes: 这么简单，没想到，吐了，取第k大个，就把k以下的都pop，然后小根堆最下面的就是
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


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest2(3, [4,5,8,2])
obj.add(3)  # 4
obj.add(5)  # return 5
obj.add(10)  # return 5
obj.add(9)   # return 8
obj.add(4)   # return 8

obj = KthLargest2(1, [])
obj.add(-3)  # -3
obj.add(-2)  # -2
obj.add(-4)  # -2
obj.add(0)   # 0
obj.add(4)   # 4






