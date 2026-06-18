# 698. Partition to K Equal Sum Subsets

# Backtracking
# Time: O(k2^n)
# Space: O(n)
# 2023.08.01: no
# notes: from each number's view, decide which bucket to drop it in;
#        sort to prune, and mark used numbers so they can be skipped
class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k > len(nums):
            return False
        sum_num = sum(nums)
        if sum_num % k != 0:
            return False
        else:
            target = sum_num // k
        bucket = [0]*k
        nums.sort(reverse=True)
        def backtrack(nums, index, bucket, target):
            if index == len(nums):
                for i in range(len(bucket)):
                    if bucket[i] != target:
                        return False
                return True
            for i in range(len(bucket)):
                if bucket[i] + nums[index] > target:
                    continue
                bucket[i] += nums[index]
                if backtrack(nums, index+1, bucket, target):
                    return True
                bucket[i] -= nums[index]
            return False
        return backtrack(nums, 0, bucket, target)


# Backtracking
# Time: O(n^2)
# Space: O(n)
# 2023.08.01: no
# notes: from each bucket's view; only move to the next bucket once
#        the current one is exactly filled
class Solution2:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # rule out some basic cases
        if k > len(nums):
            return False
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        used = [False] * len(nums)
        target = total_sum // k
        # bucket k starts empty, begin choosing from nums[0]
        def backtrack(k, bucket, nums, start, used, target):
            if k == 0:
                return True
            if bucket == target:
                return backtrack(k - 1, 0, nums, 0, used, target)
            for i in range(start, len(nums)):
                if used[i]:
                    continue
                if bucket + nums[i] > target:
                    continue
                used[i] = True
                if backtrack(k, bucket + nums[i], nums, i + 1, used, target):
                    return True
                used[i] = False
            return False
        return backtrack(k, 0, nums, 0, used, target)


# Backtracking
# Time: O(n^2)
# Space: O(n)
# 2023.08.01: no
# notes: bucket's view again; track used numbers as a bitmask and
#        memoize states to skip repeated work
class Solution3:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        memo = {}

        def backtrack(k, bucket, nums, start, used, target):
            # base case
            if k == 0:
                # all buckets filled and nums fully used
                return True
            if bucket == target:
                res = backtrack(k - 1, 0, nums, 0, used, target)
                # cache the result
                memo[used] = res
                return res
            if used in memo:
                # avoid redundant computation
                return memo[used]

            for i in range(start, len(nums)):
                if ((used >> i) & 1) == 1:
                    # nums[i] already placed in another bucket
                    continue
                if nums[i] + bucket > target:
                    continue
                used |= 1 << i
                bucket += nums[i]
                if backtrack(k, bucket, nums, i + 1, used, target):
                    return True
                used ^= 1 << i
                bucket -= nums[i]

            return False

        # make sure k is not larger than len(nums)
        if k > len(nums):
            return False
        sum_nums = sum(nums)
        if sum_nums % k != 0:
            return False
        used = 0  # bitmask trick
        target = sum_nums // k  # target sum per bucket
        # bucket k starts empty, begin choosing from nums[0]
        return backtrack(k, 0, nums, 0, used, target)


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.canPartitionKSubsets([4,3,2,3,5,2,1], 4) is True
    assert sol.canPartitionKSubsets([1,2,3,4], 3) is False
    assert sol.canPartitionKSubsets([2,2,2,2,3,4,5], 4) is False
    assert sol.canPartitionKSubsets([4,4], 2) is True
