# 90. Subsets II

# Backtracking
# Time: O(n2^n)
# Space: O(n)
# 2023.08.02: no
# notes: like normal subsets, but sort first and skip a value
#        equal to the previous one at the same level to avoid dups
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first, curr):
            output.append(curr[:])
            for i in range(first, n):
                if i > first and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        output = []
        n = len(nums)
        nums = sorted(nums)
        backtrack(0,[])
        return output


# Bitmasking
# Time: O(n2^n)
# Space: O(n)
# 2023.08.02: no
# notes: same as 78's bitmask, plus a seen set to drop duplicates
class Solution2:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        n = len(nums)
        nums.sort()

        maxNumberOfSubsets = 1 << n
        seen = set()

        for subsetIndex in range(maxNumberOfSubsets):
            currentSubset = []
            hashcode = []
            for j in range(n):
                mask = 1 << j
                isSet = mask & subsetIndex
                if isSet != 0:
                    currentSubset.append(nums[j])
                    hashcode.append(str(nums[j]))

            # Generate the hashcode as a comma-separated string.
            hashcode = ",".join(hashcode)

            if hashcode not in seen:
                seen.add(hashcode)
                subsets.append(currentSubset)

        return subsets


# Bitmasking
# Time: O(n2^n)
# Space: O(logn)
# 2023.08.02: no
# notes: if a value repeats the previous one, only extend the
#        subsets made in the last step; otherwise extend all
class Solution3:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        subsets = [[]]
        subset_size = 0
        for i in range(len(nums)):
            starting_index = subset_size if i >= 1 and nums[i] == nums[i - 1] else 0
            # subset_size refers to the size of the subset in the previous step.
            # This value also indicates the starting index of the subsets generated in this step.
            subset_size = len(subsets)
            for j in range(starting_index, subset_size):
                current_subset = subsets[j][:]
                current_subset.append(nums[i])
                subsets.append(current_subset)

        return subsets


# Tests:
def norm(res):
    return sorted(sorted(s) for s in res)


for sol in (Solution(), Solution2(), Solution3()):
    assert norm(sol.subsetsWithDup([1,2,2])) == \
        [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    assert norm(sol.subsetsWithDup([0])) == [[], [0]]
    assert norm(sol.subsetsWithDup([4,4,4,1,4])) == \
        norm([[], [1], [4], [4,4], [4,4,4], [4,4,4,4],
              [1,4], [1,4,4], [1,4,4,4], [1,4,4,4,4]])
