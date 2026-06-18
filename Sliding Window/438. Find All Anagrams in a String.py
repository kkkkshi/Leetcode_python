# 438. Find All Anagrams in a String

# Sliding Window with Hashmap Approach
# Time: O(n)
# Space: O(1)
# 2023.06.20: yes
# notes: the key thing to update each step is valid and the window
from collections import Counter


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        valid, left, right = 0, 0, 0
        needs, window = Counter(p), {}
        results = []
        while right < len(s):
            c = s[right]
            right += 1
            if c in needs:
                window[c] = window.get(c,0) + 1
                if needs[c] == window[c]:
                    valid += 1

            while right - left >= len(p):
                if valid == len(needs):
                    results.append(left)
                d = s[left]
                left += 1
                if d in needs:
                    if needs[d] == window[d]:
                        valid -= 1
                    window[d] -= 1
        return results


# Sliding Window with Array
# Time: O(n)
# Space: O(1)
# 2023.06.20: no
# notes: same idea, track valid and the window changes, then check
#        whether the counts match
class Solution2:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count, s_count = [0] * 26, [0] * 26
        # build reference array using string p
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        output = []
        # sliding window on the string s
        for i in range(ns):
            # add one more letter
            # on the right side of the window
            s_count[ord(s[i]) - ord('a')] += 1
            # remove one letter
            # from the left side of the window
            if i >= np:
                s_count[ord(s[i - np]) - ord('a')] -= 1
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)

        return output


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert sol.findAnagrams("abab", "ab") == [0, 1, 2]
    assert sol.findAnagrams("aa", "bb") == []
