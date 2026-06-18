# 2068. Check Whether Two Strings are Almost Equivalent

from collections import Counter


# Counter Approach
# Time: O(n)
# Space: O(1)
# notes: compare letter counts; almost equivalent if every letter's
#        count differs by at most 3 between the two words
class Solution:
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        return all(v < 4 for v in ((Counter(word1) - Counter(word2)) + (Counter(word2) - Counter(word1))).values())


# Tests:
for sol in (Solution(),):
    assert sol.checkAlmostEquivalent("aaaa", "bccb") is False
    assert sol.checkAlmostEquivalent("abcdeef", "abaaacc") is True
    assert sol.checkAlmostEquivalent("cccddabba", "babababab") is True
    assert sol.checkAlmostEquivalent("", "") is True
