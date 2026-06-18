# 155. Min Stack

# stack Approach
# Time: O(1)
# Space: O(n)
# 2023.07.18: yes
# notes: store (value, running_min) pairs so getMin is the top's
#        second field
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        # If the stack is empty, then the min value
        # must just be the first value we add
        if not self.stack:
            self.stack.append((x, x))
            return

        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Two stack Approach
# Time: O(1)
# Space: O(n)
# 2023.07.18: no
# notes: keep a separate stack that only holds non-increasing mins
class MinStack2:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Two stack improved Approach
# Time: O(1)
# Space: O(n)
# 2023.07.18: no
# notes: store [value, count] on the min stack to handle repeated
#        minimums without duplicating entries
class MinStack3:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:

        # We always put the number onto the main stack.
        self.stack.append(x)

        # If the min stack is empty, or this number is smaller than
        # the top of the min stack, put it on with a count of 1.
        if not self.min_stack or x < self.min_stack[-1][0]:
            self.min_stack.append([x, 1])

        # Else if this number is equal to what's currently at the top
        # of the min stack, then increment the count at the top by 1.
        elif x == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def pop(self) -> None:

        # If the top of min stack is the same as the top of stack
        # then we need to decrement the count at the top by 1.
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1

        # If the count at the top of min stack is now 0, then remove
        # that value as we're done with it.
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()

        # And like before, pop the top of the main stack.
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]


# Tests:
for cls in (MinStack, MinStack2, MinStack3):
    s = cls()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2
    s.push(-2)
    assert s.getMin() == -2
    s.pop()
    assert s.getMin() == -2
