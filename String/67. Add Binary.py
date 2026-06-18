# 67. Add Binary

# Bit Manipulation
# Time: O(n)
# Space: O(1)
# 2023.08.02: yes
# notes: parse both as ints, add, format the sum back to binary
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]


# Bit-by-Bit Computation
# Time: O(max(M,N))
# Space: O(max(M,N))
# 2023.08.02: no
# notes: pad to equal length, add bit by bit keeping a carry
class Solution2:
    def addBinary(self, a, b) -> str:
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')

            carry //= 2

        if carry == 1:
            answer.append('1')
        answer.reverse()

        return ''.join(answer)


# Bit Manipulation
# Time: O(N+M)
# Space: O(max(M,N))
# 2023.08.02: no
# notes: xor gives the sum without carry, (x & y) << 1 is the carry;
#        loop until the carry is consumed
class Solution3:
    def addBinary(self, a, b) -> str:
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.addBinary("11", "1") == "100"
    assert sol.addBinary("1010", "1011") == "10101"
    assert sol.addBinary("0", "0") == "0"
    assert sol.addBinary("1", "0") == "1"
