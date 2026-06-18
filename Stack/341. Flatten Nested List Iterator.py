# 341. Flatten Nested List Iterator

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, val=None, nested_list=None):
        self.val = val
        self.list = nested_list

    def isInteger(self):
        return self.val is not None

    def getInteger(self):
        return self.val

    def getList(self):
        return self.list


def build(data):
    """Build a list of NestedInteger from a nested python list."""
    result = []
    for item in data:
        if isinstance(item, list):
            result.append(NestedInteger(nested_list=build(item)))
        else:
            result.append(NestedInteger(val=item))
    return result


def flatten(iterator):
    """Drain an iterator into a plain list using next/hasNext."""
    out = []
    while iterator.hasNext():
        out.append(iterator.next())
    return out


# Make a Flat List with Recursion Approach
# Time: constructor: O(n+l), next: O(1), hasnext: O(1)
# Space: O(n+d)
# 2023.07.02: no
# notes: like walking a multi-way tree, flatten everything upfront
class NestedIterator:

    def __init__(self, nestedList):
        def flatten_list(nested_list):
            for nested_integer in nested_list:
                if nested_integer.isInteger():
                    self._integers.append(nested_integer.getInteger())
                else:
                    flatten_list(nested_integer.getList())
        self._integers = []
        self._position = -1 # Pointer to previous returned.
        flatten_list(nestedList)

    def next(self):
        self._position += 1
        return self._integers[self._position]

    def hasNext(self):
        return self._position + 1 < len(self._integers)


# Stack Approach
# Time: constructor: O(n+l), next: O(1), hasnext: O(1), makeStackTopAnInteger: O(1)
# Space: O(n+d)
# 2023.07.02: no
class NestedIterator2:

    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))

    def next(self) -> int:
        self.make_stack_top_an_integer()
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        self.make_stack_top_an_integer()
        return len(self.stack) > 0

    def make_stack_top_an_integer(self):
        # While the stack contains a nested list at the top...
        while self.stack and not self.stack[-1].isInteger():
            # Unpack the list at the top by putting its items onto
            # the stack in reverse order.
            self.stack.extend(reversed(self.stack.pop().getList()))


# Two Stacks Approach
# Time: constructor: O(1), next: O(1), hasnext: O(1), makeStackTopAnInteger: O(1)
# Space: O(d)
# 2023.07.02: no
# notes: one stack holds the position, lazily unpack lists on demand
class NestedIterator3:

    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]

    def make_stack_top_an_integer(self):

        while self.stack:

            # Essential for readability :)
            current_list = self.stack[-1][0]
            current_index = self.stack[-1][1]

            # If the top list is used up, pop it and its index.
            if len(current_list) == current_index:
                self.stack.pop()
                continue

            # Otherwise, if it's already an integer, we don't need
            # to do anything.
            if current_list[current_index].isInteger():
                break

            # Otherwise, it must be a list. We need to increment the index
            # on the previous list, and add the new list.
            new_list = current_list[current_index].getList()
            self.stack[-1][1] += 1  # Increment old.
            self.stack.append([new_list, 0])

    def next(self) -> int:
        self.make_stack_top_an_integer()
        current_list = self.stack[-1][0]
        current_index = self.stack[-1][1]
        self.stack[-1][1] += 1
        return current_list[current_index].getInteger()

    def hasNext(self) -> bool:
        self.make_stack_top_an_integer()
        return len(self.stack) > 0


# Using a Generator
# Time: constructor: O(1), next: O(1), hasnext: O(1), makeStackTopAnInteger: O(1)
# Space: O(d)
# 2023.07.02: no
class NestedIterator4:

    def __init__(self, nestedList: [NestedInteger]):
        # Get a generator object from the generator function, passing in
        # nestedList as the parameter.
        self._generator = self._int_generator(nestedList)
        # All values are placed here before being returned.
        self._peeked = None

    # This is the generator function. It can be used to create generator
    # objects.
    def _int_generator(self, nested_list):
        # This code is the same as Approach 1. It's a recursive DFS.
        for nested in nested_list:
            if nested.isInteger():
                yield nested.getInteger()
            else:
                # We always use "yield from" on recursive generator calls.
                yield from self._int_generator(nested.getList())
        # Will automatically raise a StopIteration.

    def next(self) -> int:
        # Check there are integers left, and if so, then this will
        # also put one into self._peeked.
        if not self.hasNext(): return None
        # Return the value of self._peeked, also clearing it.
        next_integer, self._peeked = self._peeked, None
        return next_integer

    def hasNext(self) -> bool:
        if self._peeked is not None: return True
        try:  # Get another integer out of the generator.
            self._peeked = next(self._generator)
            return True
        except:  # The generator is finished so raised StopIteration.
            return False


# Tests:
for It in (NestedIterator, NestedIterator2, NestedIterator3, NestedIterator4):
    assert flatten(It(build([[1, 1], 2, [1, 1]]))) == [1, 1, 2, 1, 1]
    assert flatten(It(build([1, [4, [6]]]))) == [1, 4, 6]
    assert flatten(It(build([]))) == []
