# Recursion
# Time: O(n)
# Space: O(1)
# 2023.08.05: no
# notes: 根据index来计数，遇到这个Index就*-1，如果重复遇到了负数的数，就说明是duplicate，如果是正数，说明是没出现的数
class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        dup = -1
        for i in range(n):
            # 现在的元素是从 1 开始的
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                dup = abs(nums[i])
            else:
                nums[index] *= -1

        missing = -1
        for i in range(n):
            if nums[i] > 0:
                # 将索引转换成元素
                missing = i + 1

        return [dup, missing]

# Using XOR
# Time: O(n)
# Space: O(1)
# 2023.09.03: no
# notes: 第一遍遍历和第二遍，第一遍所有数字，第二遍所有index, 找到missing number ^ repeated number，假设为xor
# 找到xor中的right most bit,遍历第三遍，把所有数字根据这个bit分类成两类，bit = 1/ bit = 0
# 第四遍第五遍，把分类的的bit1和bit0再次根据index遍历一遍，找到repeated 和missing，因为repeated 和missing必定存在两个分类中
class Solution2:
    def findErrorNums(self, nums):
        xor = 0
        xor0 = 0
        xor1 = 0

        for n in nums:
            xor ^= n

        for i in range(1, len(nums) + 1):
            xor ^= i

        rightmostbit = xor & ~(xor - 1)

        for n in nums:
            if n & rightmostbit != 0:
                xor1 ^= n
            else:
                xor0 ^= n

        for i in range(1, len(nums) + 1):
            if i & rightmostbit != 0:
                xor1 ^= i
            else:
                xor0 ^= i

        for i in range(len(nums)):
            if nums[i] == xor0:
                return [xor0, xor1]

        return [xor1, xor0]


# Example usage:
# solution = Solution()
# result = solution.findErrorNums([1, 2, 2, 4])
# print(result)


# Tests:
test = Solution()
test.findErrorNums([1,2,2,4])