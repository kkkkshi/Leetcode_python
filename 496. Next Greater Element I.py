# 496. Next Greater Element I

# Using Stack Approach
# Time: O(n)
# Space: O(n)
# 2023.07.14: yes
# notes: good: keeps order. bad: harder to follow.
# scan nums2 right to left; pop everything <= current, map the
# current to the stack top (or -1 if empty), then push current
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def greater(nums):
            n = len(nums)
            res = [0] * n
            s = []
            for i in range(n-1, -1, -1):
                while s and s[-1] <= nums[i]:
                    s.pop()
                res[i] = s[-1] if s else -1
                s.append(nums[i])
            return res
        next_nums2 = greater(nums2)
        hash_table = {}
        for i in range(len(nums2)):
            hash_table[nums2[i]] = next_nums2[i]
        next_nums1 = []
        for i in range(len(nums1)):
            next_nums1.append(hash_table[nums1[i]])
        return next_nums1


# Using Stack
# Time: O(n)
# Space: O(n)
# 2023.07.14: yes
# notes: when a bigger value shows up, map and pop the smaller
# ones; whatever is left in the stack at the end maps to -1.
# bad: output is in stack order, not input order
class Solution2:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        map = {}
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                map[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        while stack:
            map[stack.pop()] = -1
        res = []
        for num in nums1:
            res.append(map.get(num))
        return res


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert sol.nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
    assert sol.nextGreaterElement([1], [1]) == [-1]
