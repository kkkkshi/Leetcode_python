# 567. Permutation in String

from collections import Counter


# Sliding Window Approach
# Time: O(l1+ (l2-l1)), l1 is length of s1, l2 is length of s2
# Space: O(1)
# 2023.06.20: no
# notes: a permutation of s1 is a fixed-length substring, so slide a
#        window of len(s1) and check all needed counts are matched
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        needs, window = Counter(s1), {}
        valid, left, right = 0, 0, 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in needs:
                window[c] = window.get(c, 0) + 1
                if window[c] == needs[c]:
                    valid += 1
            while right - left >= len(s1):
                if valid == len(needs):
                    return True
                d = s2[left]
                left += 1
                if d in needs:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1
        return False


# Optimized Sliding Window Approach
# Time: O(l1+ 26*(l2-l1)), l1 is length of s1, l2 is length of s2
# Space: O(1)
# 2023.06.20: no
# notes: keep two count arrays and compare; each right shift updates
#        the counts and how many letters still match
class Solution2:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        s1map = [0] * 26
        s2map = [0] * 26

        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord('a')] += 1
            s2map[ord(s2[i]) - ord('a')] += 1

        count = 0
        for i in range(26):
            if s1map[i] == s2map[i]:
                count += 1

        for i in range(len(s2) - len(s1)):
            r = ord(s2[i + len(s1)]) - ord('a')
            l = ord(s2[i]) - ord('a')

            if count == 26:
                return True

            s2map[r] += 1
            if s2map[r] == s1map[r]:
                count += 1
            elif s2map[r] == s1map[r] + 1:
                count -= 1

            s2map[l] -= 1
            if s2map[l] == s1map[l]:
                count += 1
            elif s2map[l] == s1map[l] - 1:
                count -= 1

        return count == 26


# Using sorting Approach
# Time: O(l1*logl1+ l1*logl1*(l2-l1)), l1 is length of s1, l2 is length of s2
# Space: O(l1)
# 2023.06.20: no
# notes: easiest to write but slow; turns each window into a sorted
#        array and compares it to sorted s1
class Solution3:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1 = self.sort(s1)
        for i in range(len(s2) - len(s1) + 1):
            if s1 == self.sort(s2[i:i + len(s1)]):
                return True
        return False

    def sort(self, s: str) -> str:
        return ''.join(sorted(s))


# Using hashmap Approach
# Time: O(l1*logl1+ l1*logl1*(l2-l1)), l1 is length of s1, l2 is length of s2
# Space: O(l1)
# 2023.06.20: no
class Solution4:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        s1map = {}
        for char in s1:
            s1map[char] = s1map.get(char, 0) + 1

        for i in range(len(s2) - len(s1) + 1):
            s2map = {}
            for j in range(len(s1)):
                s2map[s2[i + j]] = s2map.get(s2[i + j], 0) + 1
            if self.matches(s1map, s2map):
                return True
        return False

    def matches(self, s1map: dict, s2map: dict) -> bool:
        for key in s1map:
            if s1map[key] - s2map.get(key, -1) != 0:
                return False
        return True


# Using Array Approach
# Time: O(l1+ 26*l1*(l2-l1)), l1 is length of s1, l2 is length of s2
# Space: O(l1)
# 2023.06.20: no
class Solution5:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        s1map = [0] * 26
        for char in s1:
            s1map[ord(char) - ord('a')] += 1
        for i in range(len(s2) - len(s1) + 1):
            s2map = [0] * 26
            for j in range(len(s1)):
                s2map[ord(s2[i + j]) - ord('a')] += 1
            if self.matches(s1map, s2map):
                return True
        return False

    def matches(self, s1map, s2map):
        for i in range(26):
            if s1map[i] != s2map[i]:
                return False
        return True


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4(), Solution5()):
    assert sol.checkInclusion(s1="ab", s2="eidbaooo") is True
    assert sol.checkInclusion(s1="ab", s2="eidboaoo") is False
    assert sol.checkInclusion(s1="a", s2="a") is True
    assert sol.checkInclusion(s1="abc", s2="ab") is False
