# 1567. Maximum Length of Subarray With Positive Product

# Recursion
# Time: O(n)
# Space: O(1)
# 2023.08.17: no
# notes: see https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/solutions/820072/easy-soultion-with-dry-run-java/
#        track lengths of positive and negative runs; on a
#        negative number swap them, then update the answer
class Solution:
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive = 0  # longest run so far with positive product
        negative = 0  # longest run so far with negative product
        res = 0
        for num in nums:
            temp = num
            if temp == 0:
                positive = 0
                negative = 0
            elif temp > 0:   # current number is positive
                positive += 1  # positive length always grows by 1
                negative = 0 if negative == 0 else negative + 1  # no negative run yet stays 0
                # otherwise the negative length grows by 1
            else:
                # swap positive and negative; same steps as above,
                # but the condition is always negative == 0
                x = positive # current number is negative, save old positive length
                positive = 0 if negative == 0 else negative + 1 # no prior negative run
                # swap positive and negative; positive is 0 since no positive run yet
                # otherwise after the swap positive grows by 1
                negative = x + 1  # after swap the old positive had not grown yet, add 1
            res = max(res, positive)  # answer is the longest positive run
        return res


# Tests:
for sol in (Solution(),):
    assert sol.getMaxLen([1, -2, -3, 4]) == 4
    assert sol.getMaxLen([0, 1, -2, -3, -4]) == 3
    assert sol.getMaxLen([-1, -2, -3, 0, 1]) == 2
    assert sol.getMaxLen([-1, 2]) == 1
