# 295. Find Median from Data Stream

# Two Heaps Approach (best approach)
# Time: O(logn)
# Space: O(n)
# 2023.07.17: yes
# notes: keep a max-heap of the smaller half and a min-heap of the
#        larger half so the median sits at the two tops
from heapq import *
class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0])/2
        else:
            return float(self.large[0])


# Sorting Approach (not good)
# Time: O(nlogn)
# Space: O(n)
# 2023.07.17: yes
# notes: brute force, keep a sorted list, slow but simple
import bisect

class MedianFinder2:
    def __init__(self):
        self.store = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        bisect.insort(self.store, num)

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.store)
        if n % 2 == 1:
            return self.store[n // 2]
        else:
            mid = n // 2
            return (self.store[mid - 1] + self.store[mid]) / 2.0


# Insertion Sort Approach (not good)
# Time: O(n)
# Space: O(n)
# 2023.07.17: no
# notes: same sorted-list idea, inserting with bisect_left
import bisect
class MedianFinder3:
    def __init__(self):
        self.store = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.store:
            self.store.append(num)
        else:
            bisect.insort_left(self.store, num)

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.store)
        if n % 2 == 1:
            return self.store[n // 2]
        else:
            mid = n // 2
            return (self.store[mid - 1] + self.store[mid]) / 2.0


# Tests:
for cls in (MedianFinder, MedianFinder2, MedianFinder3):
    obj = cls()
    obj.addNum(1)
    obj.addNum(2)
    assert obj.findMedian() == 1.5
    obj.addNum(3)
    assert obj.findMedian() == 2.0
    obj.addNum(4)
    assert obj.findMedian() == 2.5
