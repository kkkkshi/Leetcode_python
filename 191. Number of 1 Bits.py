# 191. Number of 1 Bits

# Bit Manipulation
# Time: O(1)
# Space: O(1)
# 2023.08.02: yes
# notes: n & (n - 1) clears the lowest set bit; count the iterations
class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count


# Bit Manipulation
# Time: O(n^2)
# Space: O(n)
# 2023.08.02: no
# notes: slide a mask over all 32 bits and count the ones that are set
class Solution2:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = 0
        mask = 1
        for i in range(32):
            if n & mask != 0:
                bits += 1
            mask <<= 1
        return bits


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.hammingWeight(0b00000000000000000000000000001011) == 3
    assert sol.hammingWeight(0b00000000000000000000000010000000) == 1
    assert sol.hammingWeight(0b11111111111111111111111111111101) == 31
    assert sol.hammingWeight(0) == 0
