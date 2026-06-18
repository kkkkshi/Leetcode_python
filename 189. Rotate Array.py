# 189. Rotate Array

# Brute Force
# Time: O(nk)
# Space: O(1)
# notes: pop the last element and insert it at the front, k times
class Solution:
    # time exceed
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())
        return nums


# Extra Array
# Time: O(n)
# Space: O(n)
# notes: place each element at (i + k) % n in a copy, then write back
class Solution2:
    # space exceed
    def rotate(self, nums, k):
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a


# Cyclic Replacement
# Time: O(n)
# Space: O(1)
# notes: move elements along their cycles, shifting each by k in place
class Solution3:
    # excellent solution
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1


# Reverse
# Time: O(n)
# Space: O(1)
# notes: reverse the whole array, then reverse the first k and the
#        rest separately
class Solution4:
    # best solution, but hard to think
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    a = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(a, 3)
    assert a == [5, 6, 7, 1, 2, 3, 4]
    b = [-1, -100, 3, 99]
    sol.rotate(b, 2)
    assert b == [3, 99, -1, -100]
    c = [1, 2]
    sol.rotate(c, 3)
    assert c == [2, 1]
