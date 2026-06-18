# 242. Valid Anagram

# Frequency Counter Approach
# Time: O(n)
# Space: O(1)
# 2023.06.23: yes
# notes: count chars of s, subtract using t; all counts zero means
#        they are anagrams
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dic = {}
        for c in s:
            s_dic[c] = s_dic.get(c,0) +1
        for d in t:
            if d in s_dic:
                s_dic[d] -= 1
            else:
                return False
        return all(value == 0 for value in s_dic.values())


# Sorting Approach
# Time: O(nlogn)
# Space: O(1)
# 2023.06.23: yes
# notes: equal length and equal sorted chars means anagram
class Solution2:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        str1 = sorted(s)
        str2 = sorted(t)
        return str1 == str2


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False
    assert sol.isAnagram("a", "a") is True
    assert sol.isAnagram("ab", "a") is False
