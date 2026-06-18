# 371. Sum of Two Integers

# Bit Manipulation: Easy and Language-Independent
# Time: O(1)
# Space: O(1)
# 2023.08.02: yes
# notes: reuse the prior trick answer = x ^ y, carry = (x & y) << 1,
#        then x, y = answer, carry to fold in the carry/borrow
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x, y = abs(a), abs(b)
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b, a)

        # abs(a) >= abs(b) -->
        # a determines the sign
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # sum of two positive integers x + y
            # where x > y
            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry
        else:
            # difference of two integers x - y
            # where x > y
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow

        return x * sign


# Bit Manipulation: Short Language-Specific Solution
# Time: O(1)
# Space: O(1)
# 2023.08.02: yes
# notes: this relies on python's own behavior, skip for now
class Solution2:
    def getSum(self, a: int, b: int) -> int:
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.getSum(1, 2) == 3
    assert sol.getSum(2, 3) == 5
    assert sol.getSum(-2, 3) == 1
    assert sol.getSum(-1, -1) == -2
    assert sol.getSum(0, 0) == 0
