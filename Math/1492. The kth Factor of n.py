# 1492. The kth Factor of n

# Math
# Time: O(logn)
# Space: O(1)
# 2023.08.17: yes
# notes: collect factors up to sqrt(n); the larger half mirrors
#        the smaller half via n // factor
class Solution:
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res = []
        unique = False
        for i in range(1,n+1):
            if i*i == n:
                res.append(i)
                unique = True
                break
            elif i*i > n:
                break
            if n % i == 0:
                res.append(i)
        if k-1 < len(res):
            return res[k-1]
        elif unique:
            if len(res) * 2 - k - 1 < 0:
                return -1
            return int(n / res[len(res) * 2 - k - 1])
        else:
            if len(res) * 2 - k <0:
                return -1
            return int(n/res[len(res)*2-k])


# Math
# Time: O(logn)
# Space: O(1)
# 2023.08.17: yes
# notes: simpler version, same sqrt idea
class Solution2:
    def kthFactor(self, n: int, k: int) -> int:
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        divisors, sqrt_n = [], int(n ** 0.5)
        for x in range(1, sqrt_n + 1):
            if n % x == 0:
                k -= 1
                divisors.append(x)
                if k == 0:
                    return x

        # If n is a perfect square
        # we have to skip the duplicate
        # in the divisor list
        if (sqrt_n * sqrt_n == n):
            k += 1

        n_div = len(divisors)
        return n // divisors[n_div - k] if k <= n_div else -1


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.kthFactor(12, 3) == 3
    assert sol.kthFactor(7, 2) == 7
    assert sol.kthFactor(4, 4) == -1
    assert sol.kthFactor(1, 1) == 1
