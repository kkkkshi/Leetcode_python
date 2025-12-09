# Binary Search
# Time: O(logn)
# Space: O(1)
# 2024.06.06: yes
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
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
class Solution2:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num