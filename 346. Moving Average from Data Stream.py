# 346. Moving Average from Data Stream

from collections import deque


# Double-ended Queue
# Time: O(1)
# Space: O(n)
# 2023.07.07: no
# notes: keep a window deque and a running sum, drop the oldest
#        value once the window is full
class MovingAverage:

    def __init__(self, size):
        """
        :type size: int
        """
        self.window = deque()
        self.window_sum = 0
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.window) >= self.size:
            temp = self.window.popleft()
            self.window_sum -= temp

        self.window.append(val)
        self.window_sum += val
        return self.window_sum/len(self.window)


# Circular Queue with Array
# Time: O(1)
# Space: O(n)
# 2023.07.07: no
# notes: fixed array used as a ring buffer; subtract the value
#        being overwritten and add the new one
class MovingAverage2:
    def __init__(self, size: int):
        """
        :type size: int
        """
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        # number of elements seen so far
        self.count = 0

    def next(self, val: int) -> float:
        """
        :type val: int
        :rtype: float
        """
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # move on to the next head
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)


# Tests:
for cls in (MovingAverage, MovingAverage2):
    obj = cls(3)
    assert obj.next(1) == 1.0
    assert obj.next(10) == 5.5
    assert obj.next(3) == (1 + 10 + 3) / 3
    assert obj.next(5) == (10 + 3 + 5) / 3
