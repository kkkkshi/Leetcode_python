# 338. Counting Bits

# Pop Count
# Time: O(nlogn)
# Space: O(1)
# 2023.08.02: yes
# notes: for each number count its set bits one by one
class Solution:
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def pop_count(x):
            count = 0
            while x != 0:
                x &= x - 1  # zeroing out the least significant nonzero bit
                count += 1
            return count

        ans = [0] * (n + 1)
        for x in range(n + 1):
            ans[x] = pop_count(x)

        return ans


# DP + Most Significant Bit
# Time: O(n)
# Space: O(1)
# 2023.08.02: yes
# notes: dp builds [b, 2b) from [0, b); a left shift means *2 so
#        the shifted range reuses the already computed counts
class Solution2:
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n + 1)
        x = 0
        b = 1

        # [0, b) is calculated
        while b <= n:
            # generate [b, 2b) or [b, n) from [0, b)
            while x < b and x + b <= n:
                ans[x + b] = ans[x] + 1
                x += 1
            x = 0  # reset x
            b <<= 1  # b = 2b

        return ans


# DP + Least Significant Bit
# Time: O(n)
# Space: O(1)
# 2023.08.02: yes
# notes: count of x is count of x>>1 plus the lowest bit, since a
#        right shift drops one bit and x&1 tells if it was set
class Solution3:
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            # x // 2 is x >> 1 and x % 2 is x & 1
            ans[x] = ans[x >> 1] + (x & 1)
        return ans


# DP + Last Set Bit
# Time: O(n)
# Space: O(1)
# 2023.08.02: yes
# notes: x & (x-1) clears the lowest set bit, take that value
#        and add 1
class Solution4:
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.countBits(0) == [0]
    assert sol.countBits(2) == [0, 1, 1]
    assert sol.countBits(5) == [0, 1, 1, 2, 1, 2]
