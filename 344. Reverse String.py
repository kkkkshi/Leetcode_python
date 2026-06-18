# 344. Reverse String

# Two Pointers Approach (best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.18: yes
# notes: swap the two ends and move both pointers inward
class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        lp, rp = 0, len(s)-1
        while lp < rp:
            s[lp], s[rp] = s[rp], s[lp]
            lp+= 1
            rp -=1
        return


# Recursion Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.18: yes
# notes: only here as an alternative; not really fit for the
#        problem, a roundabout way to do a simple swap
class Solution2:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None
        """
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)
        helper(0, len(s) - 1)


# Tests:
for sol in (Solution(), Solution2()):
    s = ['a', 'b', 'c']
    sol.reverseString(s)
    assert s == ['c', 'b', 'a']
    s = []
    sol.reverseString(s)
    assert s == []
    s = ['a', 'b']
    sol.reverseString(s)
    assert s == ['b', 'a']
