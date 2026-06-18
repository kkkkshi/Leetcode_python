# 225. Implement Stack using Queues

import queue
from collections import deque


# Deque Approach
# Time: O(n)
# Space: O(n)
# 2023.07.07: yes
# notes: a deque already supports push/pop from the same end, so
#        it behaves like a stack directly
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)

    def pop(self):
        """
        :rtype: int
        """
        pop = self.q.pop()
        return pop

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0


# Two Queue Approach
# Time: O(n)  # 写pop的话，pop就是O(n),其他事O(1);要不就是push O(n)，其他O(1);最后一个用的单queue,一样是O(n)
# Space: O(1)
# 2023.07.07: yes
# notes: three methods stay the same as a queue except pop; rotate
#        the queue so the last pushed element comes out
# Removes the element on top of the stack
# 1      #      # 3     # 3 2 1
# 2      # 2 1  # 2 1   #
class MyStack2:
    def __init__(self):
        self.q = deque()
        self.top_elem = 0

    def push(self, x: int):
        self.q.append(x)
        self.top_elem = x

    def pop(self) -> int:
        size = len(self.q)
        # keep the last 2 elements at the tail
        while size > 2:
            self.q.append(self.q.popleft())
            size -= 1
        # record the new tail element
        self.top_elem = self.q[0]
        self.q.append(self.q.popleft())
        # remove the previous tail element
        return self.q.popleft()

    def top(self) -> int:
        return self.top_elem

    def empty(self) -> bool:
        return len(self.q) == 0


# Tests:
for Stack in (MyStack, MyStack2):
    obj = Stack()
    obj.push(1)
    obj.push(2)
    assert obj.top() == 2
    assert obj.pop() == 2
    assert obj.top() == 1
    assert obj.empty() is False
    assert obj.pop() == 1
    assert obj.empty() is True
