# 78. Subsets

# Backtracking
# Time: O(n*2^n)
# Space: O(n)
# 2023.08.02: yes
# notes: no enter/exit tracking needed; every time we reach a new
#        state we add the current path to res
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        track = []
        def backtrack(nums, start):
            res.append(list(track))
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(nums, i + 1)
                track.pop()
        backtrack(nums, 0)
        return res


# Lexicographic (Binary Sorted) Subsets
# Time: O(n*2^n)
# Space: O(n)
# notes: very clever; increment a bit mask one by one and each mask
#        picks the elements to include
class Solution2:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        output = []

        for i in range(2 ** n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output


# Tests:
def norm(res):
    return sorted(sorted(x) for x in res)


for sol in (Solution(), Solution2()):
    assert norm(sol.subsets([1, 2, 3])) == [
        [], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]
    ]
    assert norm(sol.subsets([0])) == [[], [0]]
    assert norm(sol.subsets([])) == [[]]
