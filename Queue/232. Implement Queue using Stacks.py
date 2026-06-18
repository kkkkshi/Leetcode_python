# 232. Implement Queue using Stacks

# Two Stacks Approach
# Time: peek: O(n), other: O(1)
# Space: O(n)
# 2023.07.07: yes
# notes: peek/pop always read from s2 (reversed order); only when s2
#        is empty do we pour s1 into it
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.s2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.s2) == 0:
            # move s1 elements into s2
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s1) == 0 and len(self.s2) == 0


# Tests:
q = MyQueue()
q.push(1)
q.push(2)
assert q.peek() == 1
assert q.empty() is False
q.push(3)
assert q.pop() == 1
assert q.peek() == 2
assert q.pop() == 2
assert q.pop() == 3
assert q.empty() is True
