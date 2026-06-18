# 204. Count Primes

# Sieve of Eratosthenes
# Time: O(root(n)loglog(n)+n)
# Space: O(n)
# 2023.08.02: yes
# notes: mark multiples of each prime as composite, then count the
#        numbers still flagged prime below n
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True] * n
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count


# Tests:
for sol in (Solution(),):
    assert sol.countPrimes(10) == 4
    assert sol.countPrimes(100) == 25
    assert sol.countPrimes(2) == 0
    assert sol.countPrimes(0) == 0
