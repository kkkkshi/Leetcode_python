# 278. First Bad Version

# Binary Search Approach
# Time: O(n)
# Space: O(1)
# 2023.06.25: yes
# notes: binary search for the first version where isBadVersion is true
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid-1
            else:
                left = mid + 1
        return left if isBadVersion(left) else left-1


# Tests:
def make_is_bad(first_bad):
    def isBadVersion(version):
        return version >= first_bad
    return isBadVersion


for sol in (Solution(),):
    isBadVersion = make_is_bad(4)
    assert sol.firstBadVersion(5) == 4
    isBadVersion = make_is_bad(1)
    assert sol.firstBadVersion(1) == 1
    isBadVersion = make_is_bad(2)
    assert sol.firstBadVersion(2) == 2
