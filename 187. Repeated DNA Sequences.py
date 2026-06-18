# 187. Repeated DNA Sequences

# Rabin-Karp Approach
# Time: O(n)
# Space: O(n-l)
# 2023.06.20: yes
# notes: map each base to a base-4 digit, then slide a length-10
#        window keeping a rolling hash to spot repeats
class Solution:
    def findRepeatedDnaSequences(self, s):
        # first turn the string into an array of base-4 digits
        nums = [0] * len(s)
        for i in range(len(nums)):
            if s[i] == 'A':
                nums[i] = 0
            elif s[i] == 'G':
                nums[i] = 1
            elif s[i] == 'C':
                nums[i] = 2
            elif s[i] == 'T':
                nums[i] = 3

        # hashes seen so far
        seen = set()
        # repeated substrings collected as the result
        res = set()

        # number of digits
        L = 10
        # base
        R = 4
        # value of R^(L - 1)
        RL = R ** (L - 1)
        # rolling hash of the current window
        windowHash = 0

        # sliding window framework, time O(N)
        left, right = 0, 0
        while right < len(nums):
            # grow the window, add a digit at the lowest position
            windowHash = R * windowHash + nums[right]
            right += 1

            # window reached the required length
            if right - left == L:
                # check the hash to see if this substring appeared
                if windowHash in seen:
                    # current window substring is a repeat
                    res.add(s[left:right])
                else:
                    # not seen before, record it
                    seen.add(windowHash)
                # shrink the window, drop the highest digit
                windowHash -= nums[left] * RL
                left += 1
        # convert to the List type the problem expects
        return list(res)


# Linear-time Slice Using Substring + HashSet Approach (brute force)
# Time: O(n)
# Space: O((n-l)*l)
# 2023.06.20: yes
# notes: slide a length-10 window and store the raw substrings in a
#        set, adding to output once a substring repeats
class Solution2:
    def findRepeatedDnaSequences(self, s):
        L, n = 10, len(s)
        seen, output = set(), set()

        # iterate over all sequences of length L
        for start in range(n - L + 1):
            tmp = s[start:start + L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return output


# Bit Manipulation
# Time: O(n-l)
# Space: O((n-l)*l)
# 2023.06.20: no
# notes: don't fully get it, but the core idea is close to Rabin-Karp;
#        keep a 20-bit mask rolled forward 2 bits per step
class Solution3:
    def findRepeatedDnaSequences(self, s):
        L, n = 10, len(s)
        if n <= L:
            return []

        # convert string to the array of 2-bits integers:
        # 00_2, 01_2, 10_2 or 11_2
        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int.get(s[i]) for i in range(n)]

        bitmask = 0
        seen, output = set(), set()
        # iterate over all sequences of length L
        for start in range(n - L + 1):
            # compute bitmask of the sequence in O(1) time
            if start != 0:
                # left shift to free the last 2 bit
                bitmask <<= 2
                # add a new 2-bits number in the last two bits
                bitmask |= nums[start + L - 1]
                # unset first two bits: 2L-bit and (2L + 1)-bit
                bitmask &= ~(3 << 2 * L)
            # compute bitmask of the first sequence in O(L) time
            else:
                for i in range(L):
                    bitmask <<= 2
                    bitmask |= nums[i]
            if bitmask in seen:
                output.add(s[start:start + L])
            seen.add(bitmask)
        return output


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sorted(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) == ["AAAAACCCCC", "CCCCCAAAAA"]
    assert sorted(sol.findRepeatedDnaSequences("AAAAAAAAAAAAA")) == ["AAAAAAAAAA"]
    assert sorted(sol.findRepeatedDnaSequences("ACGT")) == []
