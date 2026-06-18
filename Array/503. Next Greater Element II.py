# 503. Next Greater Element II

# Monotonic Stack Approach (best approach)
# Time: O(n)
# Space: O(n)
# 2023.07.15: yes
# notes: store indices; handle the circular array with modulo
class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        s = []
        for i in range(2*n-1, -1, -1):
            while s and s[-1] <= nums[i%n]:
                s.pop()
            res[i%n] = -1 if not s else s[-1]
            s.append(nums[i%n])
        return res


# Tests:
for sol in (Solution(),):
    assert sol.nextGreaterElements([1, 2, 1]) == [2, -1, 2]
    assert sol.nextGreaterElements([1, 2, 3, 4, 3]) == [2, 3, 4, -1, 4]
    assert sol.nextGreaterElements([5, 4, 3, 2, 1]) == [-1, 5, 5, 5, 5]
    assert sol.nextGreaterElements([1]) == [-1]
