# 231. Power of Two

# Bit Manipulation
# Time: O(1)
# Space: O(1)
# 2023.08.02: yes
# notes: n & (n-1) clears the lowest set bit; count the bits and a
#        power of two has exactly one
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        if n < 0:
            return False
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count == 1


# Bit Manipulation
# Time: O(1)
# Space: O(1)
# 2023.08.02: yes
# notes: clear the lowest set bit with n & (n-1); a power of two
#        becomes 0 afterwards
class Solution2:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return n & (n - 1) == 0


# Bit Manipulation
# Time: O(1)
# Space: O(1)
# 2023.08.02: no
# notes: n & -n keeps only the lowest set bit; if it equals n then n
#        has a single bit, so it is a power of two
class Solution3:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return n & (-n) == n


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.isPowerOfTwo(1) is True
    assert sol.isPowerOfTwo(16) is True
    assert sol.isPowerOfTwo(9) is False
    assert sol.isPowerOfTwo(0) is False
