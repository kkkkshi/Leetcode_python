# 190. Reverse Bits

# Bit by Bit
# Time: O(1)
# Space: O(1)
# 2023.08.02: yes
# notes: take the lowest bit then shift right, repeating each step
class Solution:
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret


# Byte by Byte with Memoization
# Time: O(1)
# Space: O(1)
# 2023.08.02: yes
# notes: reverse byte order, then reverse the bits inside each byte;
#        (byte * 0x0202020202 & 0x010884422010) % 1023 flips one byte
# http://graphics.stanford.edu/~seander/bithacks.html#ReverseByteWith64BitsDiv
class Solution2:
    def reverseBits(self, n):
        ret, power = 0, 24
        cache = dict()
        while n:
            ret += self.reverseByte(n & 0xff, cache) << power
            n = n >> 8
            power -= 8
        return ret

    def reverseByte(self, byte, cache):
        if byte not in cache:
            cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023
        return cache[byte]


# Mask and Shift
# Time: O(1)
# Space: O(1)
# 2023.08.02: yes
# notes: swap halves repeatedly: 16 with 16, then 8s, 4s, 2s, 1s
# https://leetcode.com/problems/reverse-bits/editorial/
class Solution3:
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.reverseBits(0b00000010100101000001111010011100) == 964176192
    assert sol.reverseBits(0b11111111111111111111111111111101) == 3221225471
    assert sol.reverseBits(0) == 0
