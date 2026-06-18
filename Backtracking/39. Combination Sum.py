# 39. Combination Sum

# Backtracking (best approach)
# Time: O(n^(t/m+1)), t/m is height
# Space: O(t/m)
# 2023.06.24: yes
# notes: backtrack picking from start onward; reuse allowed, so the
#        recursion keeps the same index i
class Solution:
    # start is the starting index
    def backtrack(self, candidates, results, combination, start, remain):
        if remain < 0:
            return results
        elif remain == 0:
            return results.append(combination[:]) # deep copy
        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            self.backtrack(candidates, results, combination, i, remain-candidates[i])
            combination.pop()
        return results

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = self.backtrack(candidates, [], [], 0, target)
        return result


# Tests:
for sol in (Solution(),):
    assert sol.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert sol.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert sol.combinationSum([2], 1) == []
    assert sol.combinationSum([7, 3, 2], 18) == \
        [[7, 7, 2, 2], [7, 3, 3, 3, 2], [7, 3, 2, 2, 2, 2],
         [3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 2, 2, 2],
         [3, 3, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2]]
