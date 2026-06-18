# 69. Sqrt(x)

# Binary Search
# Time: O(logn)
# Space: O(1)
# 2024.06.05: yes
# notes: binary search for the largest mid with mid*mid <= x
class Solution:
    def mySqrt(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        lo, hi = 0, x
        while lo <= hi:
            mid = (lo+hi)//2
            if mid ** 2 == x:
                return mid
            elif mid **2 > x:
                hi = mid-1
            else:
                lo = mid+1
        return lo-1


# Pocket Calculator Algorithm
# Time: O(1)
# Space: O(1)
# 2024.06.05: no
# notes: pure math, sqrt via exp(0.5*log(x))
from math import e, log

class Solution2:
    def mySqrt(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left = int(e ** (0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right


# Newton's method
# Time: O(logn)
# Space: O(1)
# 2024.06.05: no
# notes: pure math, Newton iteration formula
class Solution3:
    def mySqrt(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + float(x) / x0) / 2

        return int(x1)


# Recursion + Bit Shifts
# Time: O(logn)
# Space: O(1)
# 2024.06.05: no
# notes: master's theorem, pure math
class Solution4:
    def mySqrt(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left = self.mySqrt(x >> 2) << 1
        right = left + 1
        return left if right * right > x else right


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.mySqrt(0) == 0
    assert sol.mySqrt(1) == 1
    assert sol.mySqrt(4) == 2
    assert sol.mySqrt(8) == 2
    assert sol.mySqrt(2147395600) == 46340
