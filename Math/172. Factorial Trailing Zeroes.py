# 172. Factorial Trailing Zeroes

# Counting Factors of 5 Efficiently
# Time: O(logn)
# Space: O(1)
# 2023.08.04: yes
# notes: count how many 5s, 25s, 125s, etc. divide into n
class Solution:
    def trailingZeroes(self, n):
        res = 0
        divisor = 5
        while divisor <= n:
            res += n // divisor
            divisor *= 5
        return res


# Counting Factors of 5
# Time: O(n)
# Space: O(1)
# 2023.08.04: yes
# notes: walk every multiple of 5 up to n and divide out each factor
#        of 5 it contributes
class Solution2:
    def trailingZeroes(self, n):
        zero_count = 0
        for i in range(5, n + 1, 5):
            current = i
            while current % 5 == 0:
                zero_count += 1
                current //= 5

        return zero_count


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.trailingZeroes(26) == 6
    assert sol.trailingZeroes(0) == 0
    assert sol.trailingZeroes(5) == 1
    assert sol.trailingZeroes(100) == 24
