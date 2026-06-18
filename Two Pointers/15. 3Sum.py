# 15. 3Sum

# Two Pointers Approach
# Time: O(n^2)
# Space: O(logn)
# 2023.06.24: yes
# notes: sort, fix one number, then two-pointer scan the rest;
#        skip duplicates to avoid repeated triplets
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums, i, res):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1


# Hashset Approach
# Time: O(n^2)
# Space: O(n)
# 2023.06.24: yes
# notes: for each first number, use a seen set to find the third
#        number that completes a zero sum
class Solution2:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res


# "No-Sort" Approach
# Time: O(n^2)
# Space: O(n)
# 2023.06.24: yes
# notes: same hashset idea without pre-sorting the input
class Solution3:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res


# Tests:
def norm(triplets):
    return sorted(tuple(sorted(t)) for t in triplets)


for sol in (Solution(), Solution2(), Solution3()):
    assert norm(sol.threeSum([-1, 0, 1, 2, -1, -4])) == \
        [(-1, -1, 2), (-1, 0, 1)]
    assert norm(sol.threeSum([0, 1, 1])) == []
    assert norm(sol.threeSum([0, 0, 0])) == [(0, 0, 0)]
