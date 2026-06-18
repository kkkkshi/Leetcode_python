# 3. Longest Substring Without Repeating Characters

# Sliding Window with Hashmap Approach
# Time: O(n)
# Space: O(1)
# 2023.06.20: yes
# notes: expand the window to the right; when a char count exceeds 1,
#        shrink from the left until the window has no duplicates
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right, maxlen = 0, 0, 0
        window = {}
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) +1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            maxlen = max(maxlen, right-left)
        return maxlen


# Sliding Window Optimized Approach
# Time: O(n)
# Space: O(1)
# 2023.06.20: no
# notes: record the index so left jumps straight there, no stepping
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}
        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1
        return ans


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("") == 0
    assert sol.lengthOfLongestSubstring(" ") == 1
    assert sol.lengthOfLongestSubstring("dvdf") == 3
