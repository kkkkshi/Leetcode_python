# 372. Super Pow

# Recursion
# Time: O(n)
# Space: O(1)
# 2023.08.05: no
# notes: core idea is recursion
from typing import List


class Solution:
    base = 1337  # declare a class variable base

    # declare an instance method mypow
    def mypow(self, a, k):
        a %= self.base  # take a modulo the base
        res = 1
        for _ in range(k):
            res *= a  # multiply here, a potential overflow point
            res %= self.base  # take the product modulo base
        return res

    # declare an instance method superPow
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if not b:
            return 1
        last = b.pop()  # take the last element of array b
        part1 = self.mypow(a, last)  # compute a to the last power
        part2 = self.mypow(self.superPow(a, b), 10)  # recurse: superPow(a, b[:len(b)-1]) to the 10th power
        return (part1 * part2) % self.base  # return result, take modulo each time


# Recursion
# Time: O(n)
# Space: O(1)
# 2023.08.05: no
# notes: split by parity: if b is odd a^b = a^(b-1)*a, if even
#        a^b = (a^(b//2))^2. same efficiency, just simpler to write.
# Sep 3 update: if b = m*10+d then a^b = a^d * (a^m)^10; this is the
#        key to the recursion, peeling b digit by digit.
class Solution2:
    base = 1337

    def superPow(self, a: int, b: List[int]) -> int:
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if not b:
            return 1
        last = b.pop()  # take the last element of array b
        part1 = self.mypow(a, last)  # compute a to the last power
        part2 = self.mypow(self.superPow(a, b), 10)  # recurse: superPow(a, b[:len(b)-1]) to the 10th power
        return (part1 * part2) % self.base  # return result, take modulo each time

    def mypow(self, a: int, k: int) -> int:
        if k == 0:
            return 1

        base = 1337
        a %= base

        if k % 2 == 1:
            # k is odd
            return (a * self.mypow(a, k - 1)) % base
        else:
            # k is even
            sub = self.mypow(a, k // 2)
            return (sub * sub) % base


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.superPow(2, [3]) == 8
    assert sol.superPow(2, [1, 0]) == 1024
    assert sol.superPow(1, [4, 3, 3, 8, 5, 2]) == 1
    assert sol.superPow(2147483647, [2, 0, 0]) == 1198
