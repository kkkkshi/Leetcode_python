# 46. Permutations

# Backtracking
# Time: O(n^2)
# Space: O(n)
# 2023.08.01: yes
# notes: pick each remaining number in turn, recurse, then put it
#        back to restore the pool for the next choice
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        num_length = len(nums)
        def rec(nums, cur):
            if len(cur) == num_length:
                results.append(cur[:])
                return
            for i in range(len(nums)):
                tmp = nums.pop(i)
                cur.append(tmp)
                rec(nums, cur)
                cur.pop()
                nums.insert(i, tmp)
        rec(nums,[])
        return results


# Tests:
for sol in (Solution(),):
    assert sorted(sol.permute([1,2,3])) == [
        [1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    assert sol.permute([1]) == [[1]]
    assert sorted(sol.permute([0,1])) == [[0,1],[1,0]]
