# Binary Search
# Time: O(nlogn)
# Space: O(1)
# 2023.10.29: yes
# notes: 因为Nums是1-n，每个应该只出现一次，所以计算当前这个数字，有几个比他小的
# 如果超出了应该比他小的个数，就说明，比他小的地方有重复，binary search缩小范围
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1
        while low <= high:
            cur = (low + high) // 2
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
        return duplicate

# Sum of Set Bits
# Time: O(nlogn)
# Space: O(1)
# 2023.10.29: no
# notes: 计算一个个位置上的bit，看是不是多出来的那个，如果是重复的话，bit会比原来的多，记录即可，只需要考虑正的，负数证明没出现过
class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = 0
        n = len(nums) - 1
        bits = n.bit_length()
        for bit in range(bits):
            mask = 1 << bit
            base_count = 0
            nums_count = 0
            for i in range(n + 1):
                # If bit is set in number (i) then add 1 to base_count
                if i & mask:
                    base_count += 1

                # If bit is set in nums[i] then add 1 to nums_count
                if nums[i] & mask:
                    nums_count += 1

            # If the current bit is more frequently set in nums than it is in
            # the range [1, 2, ..., n] then it must also be set in the duplicate number.
            if nums_count - base_count > 0:
                duplicate |= mask

        return duplicate


# Floyd's algorithm (best approach)
# Time: O(nlogn)
# Space: O(1)
# 2023.10.29: yes
# notes: 通过构造Floyd's algorithm的方法，龟兔赛跑，从一个点到另一个点，必定会有循环出现，hare每次跳两步，也就是nums[nums[hare]]
# tortoise每次跳一步
class Solution3:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare

# Test:
test = Solution3()
test.findDuplicate([1,3,4,2,2])