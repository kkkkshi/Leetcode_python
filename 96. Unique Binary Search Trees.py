# 96. Unique Binary Search Trees

# Dynamic Programming Approach
# Time: O(logn)
# Space: O(h)
# 2023.06.30: no
# notes: dp; G[i] is the count for i nodes, and the only real step is
#        res = left * right, the rest is init and accumulating the
#        recursion; worth revisiting later, idea is clear but hard to write
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                left = j-1
                right = i-j
                G[i] += G[left] * G[right]
        return G[n]


# Recursion Approach
# Time: O(n^2)
# Space: O(n)
# 2023.06.30: no
# notes: for each range pick every value as root, count the BSTs on the
#        left and right ranges and multiply, memoize by (lo, hi)
class Solution2:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize memo with 0 values
        self.memo = [[0] * (n + 1) for _ in range(n + 1)]
        return self.count(1, n)

    def count(self, lo, hi):
        if lo > hi:
            return 1
        # Check the memoization table
        if self.memo[lo][hi] != 0:
            return self.memo[lo][hi]

        res = 0
        for mid in range(lo, hi + 1):
            left = self.count(lo, mid - 1)  # Fixed method call
            right = self.count(mid + 1, hi)  # Fixed method call
            res += left * right   # core
        # Store the result in the memoization table
        self.memo[lo][hi] = res

        return res


# Mathematical Deduction Approach
# Time: O(n)
# Space: O(1)
# 2023.06.30: yes
# notes: compute the nth Catalan number directly with the product
#        formula C(i+1) = C(i) * 2(2i+1)/(i+2)
class Solution3:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.numTrees(1) == 1
    assert sol.numTrees(2) == 2
    assert sol.numTrees(3) == 5
    assert sol.numTrees(4) == 14
    assert sol.numTrees(5) == 42
