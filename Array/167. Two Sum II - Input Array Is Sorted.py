# 167. Two Sum II - Input Array Is Sorted

# Two Pointers Approach (best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.18: no
# notes: the window need not start aligned; since the array is sorted
#        move one pointer from the left and one from the right
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lp, rp = 0, len(numbers)-1
        while lp < rp:
            if numbers[lp] + numbers[rp] == target:
                return [lp+1, rp+1]
            elif numbers[lp] + numbers[rp] > target:
                rp -= 1
            else:
                lp += 1


# Tests:
for sol in (Solution(),):
    assert sol.twoSum([2,7,11,15], 9) == [1, 2]
    assert sol.twoSum([2,3,4], 6) == [1, 3]
    assert sol.twoSum([-1,0], -1) == [1, 2]
    assert sol.twoSum([5,25,75], 100) == [2, 3]
