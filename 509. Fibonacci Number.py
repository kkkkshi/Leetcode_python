# 509. Fibonacci Number

# Recursion
# Time: O(2^n)
# Space: O(n)
# 2023.06.20: yes
# notes: plain recursion on fib(N-1) + fib(N-2)
class Solution:
    def fib(self, N: int) -> int:
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)


# Recursion
# Time: O(n)
# Space: O(n)
# 2023.06.20: yes
# notes: bottom-up cache array, each entry sums the prior two
class Solution2:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N

        cache = [0] * (N + 1)
        cache[1] = 1
        for i in range(2, N + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[N]


# Matrix Exponentiation
# Time: O(logn)
# Space: O(logn)
# 2023.06.20: no
# notes: roll two variables instead of a full array, O(1) space
class Solution3:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if (N <= 1):
            return N
        current = 0
        prev1 = 1
        prev2 = 0
        for i in range(2, N + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current


# Matrix Exponentiation
# Time: O(n)
# Space: O(n)
# 2023.06.20: no
# notes: pure math, skipped for now
class Solution4:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if (N <= 1):
            return N

        A = [[1, 1], [1, 0]]
        self.matrix_power(A, N - 1)

        return A[0][0]

    def matrix_power(self, A, N):
        if (N <= 1):
            return A

        self.matrix_power(A, N // 2)
        self.multiply(A, A)
        B = [[1, 1], [1, 0]]

        if (N % 2 != 0):
            self.multiply(A, B)

    def multiply(self, A, B) -> None:
        x = A[0][0] * B[0][0] + A[0][1] * B[1][0]
        y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
        z = A[1][0] * B[0][0] + A[1][1] * B[1][0]
        w = A[1][0] * B[0][1] + A[1][1] * B[1][1]

        A[0][0] = x
        A[0][1] = y
        A[1][0] = z
        A[1][1] = w


# Math
# Time: O(logn)
# Space: O(1)
# 2023.06.20: no
# notes: Binet's formula, pure math, skipped
class Solution5:
    def fib(self, N: int) -> int:
        """
        :type N: int
        :rtype: int
        """
        golden_ratio = (1 + (5 ** 0.5)) / 2
        return int(round((golden_ratio ** N) / (5 ** 0.5)))


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4(), Solution5()):
    assert sol.fib(0) == 0
    assert sol.fib(1) == 1
    assert sol.fib(2) == 1
    assert sol.fib(10) == 55
    assert sol.fib(15) == 610
