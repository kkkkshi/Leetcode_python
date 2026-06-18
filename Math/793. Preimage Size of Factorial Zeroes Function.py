# 793. Preimage Size of Factorial Zeroes Function

# Counting Factors of 5 Efficiently
# Time: O(logn)
# Space: O(1)
# 2023.08.04: yes
# notes: binary search the boundary; the high bound is *10 because only
#        *10 adds another zero (*5 doesn't work in zeta)
class Solution:
    def preimageSizeFZF(self, K):

        def zeta(x):
            return x // 5 + zeta(x // 5) if x > 0 else 0

        lo, hi = K, 10 * K + 1
        while lo < hi:
            mi = (lo + hi) // 2
            zmi = zeta(mi)

            if zmi == K:
                return 5
            elif zmi < K:
                lo = mi + 1
            else:
                hi = mi

        return 0


# Tests:
for sol in (Solution(),):
    assert sol.preimageSizeFZF(0) == 5
    assert sol.preimageSizeFZF(5) == 0
    assert sol.preimageSizeFZF(3) == 5
    assert sol.preimageSizeFZF(6) == 5
