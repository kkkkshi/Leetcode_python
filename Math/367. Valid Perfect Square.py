# 367. Valid Perfect Square

# Binary Search
# Time: O(logn)
# Space: O(1)
# 2024.06.06: yes
# notes: search for a mid whose square equals num
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        :type num: int
        :rtype: bool
        """
        lo, hi = 0, num
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


# Newton's method
# Time: O(logn)
# Space: O(1)
# 2024.06.06: no
# notes: iterate x = (x + num/x)/2 until it stops decreasing
class Solution2:
    def isPerfectSquare(self, num: int) -> bool:
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True

        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.isPerfectSquare(16) is True
    assert sol.isPerfectSquare(14) is False
    assert sol.isPerfectSquare(1) is True
    assert sol.isPerfectSquare(0) is True
    assert sol.isPerfectSquare(808201) is True
