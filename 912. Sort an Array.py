# 912. Sort an Array

# Merge sort Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.06.28: no
# notes: split in half, sort each side, then merge the two sorted
#        halves back into the array in order
class Solution:
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def merge(nums, left, mid, right):
            temp = []
            start_left, start_right = left, mid + 1
            end_left, end_right = mid, right
            while start_left <= end_left and start_right <= end_right:
                if nums[start_left] <= nums[start_right]:
                    temp.append(nums[start_left])
                    start_left += 1
                else:
                    temp.append(nums[start_right])
                    start_right += 1
            while start_left <= end_left:
                temp.append(nums[start_left])
                start_left += 1
            while start_right <= end_right:
                temp.append(nums[start_right])
                start_right += 1
            nums[left:right + 1] = temp[:]

        def process(nums, left, right):
            if left < right:
                mid = (left + right) // 2
                process(nums, left, mid)
                process(nums, mid + 1, right)
                merge(nums, left, mid, right)
            return nums

        if len(nums) == 1 or len(nums) == 1:
            return nums
        return process(nums, 0, len(nums) - 1)


# Heap sort Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.06.28: no
# notes: build a max-heap, swap the root to the end, shrink the heap
#        and re-heapify, repeating until the array is sorted
class Solution2:
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # heapify: push the current node down into the max-heap until it
        # sits in the right place (heapify starting from index)
        def heapify(nums, index, heapSize):
            left = index * 2 + 1  # left child of index
            while left < heapSize:  # while the left child is in the heap
                if (left + 1 < heapSize) and (nums[left + 1] > nums[left]):  # right child in heap and bigger than left
                    largest = left + 1  # the bigger one is the right child
                else:
                    largest = left  # otherwise the bigger one is the left child
                if nums[largest] < nums[index]:  # compare node with its bigger child, pick the largest
                    largest = index
                if largest == index:  # parent is already the largest, stop sinking
                    break
                nums[largest], nums[index] = nums[index], nums[largest]  # parent not largest, swap
                index = largest  # current node becomes the bigger child
                left = index * 2 + 1  # find its left child and repeat
            return nums

        if (len(nums) == 0) or (len(nums) == 1):
            return nums
        else:
            heapSize = len(nums)
            i = heapSize - 1
            while i >= 0:  # build the max-heap from right to left
                heapify(nums, i, heapSize)
                i -= 1

        heapSize = len(nums)
        nums[0], nums[heapSize - 1] = nums[heapSize - 1], nums[0]  # move the current top to the end as sorted
        heapSize -= 1
        while heapSize > 0:
            heapify(nums, 0, heapSize)  # heapify the value just swapped to the top
            nums[0], nums[heapSize - 1] = nums[heapSize - 1], nums[0]  # repeat the process above
            heapSize -= 1  # shrink size, the last one is now sorted
        return nums


# Quick sort Approach
# Time: O(n^2)
# Space: O(n)
# 2023.06.30: no
# notes: shuffle for stable timing, pick a pivot, partition so smaller
#        values sit left of it and larger right, then recurse
import random
class Solution3:
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # shuffle the order so the time complexity stays stable
        self.shuffle(nums)
        # sort the whole array in place
        self.sort_helper(nums, 0, len(nums) - 1)
        return nums

    def sort_helper(self, nums, lo, hi):
        if lo >= hi:
            return
        # partition nums[lo..hi] so nums[lo..p-1] <= nums[p] < nums[p+1..hi]
        p = self.partition(nums, lo, hi)
        # recurse on the left half, then the right half
        self.sort_helper(nums, lo, p - 1)
        self.sort_helper(nums, p + 1, hi)

    # set the first element as pivot, then place bigger ones from the
    # right and smaller ones from pivot+1
    def partition(self, nums, lo, hi):
        pivot = nums[lo]
        i, j = lo + 1, hi
        while i <= j:
            # when this loop ends nums[i] > pivot
            while i < hi and nums[i] <= pivot:
                i += 1
            # when this loop ends nums[j] <= pivot
            while j > lo and nums[j] > pivot:
                j -= 1
            # the swap is done, break out and swap the pivot in
            if i >= j:
                break
            # not done yet, swap the out-of-place values
            nums[i], nums[j] = nums[j], nums[i]
        nums[lo], nums[j] = nums[j], nums[lo]
        return j

    def shuffle(self, nums):
        n = len(nums)
        for i in range(n):
            r = i + random.randint(0, n - i - 1)
            nums[i], nums[r] = nums[r], nums[i]


# Count sort Approach
# Time: O(n+k)
# Space: O(n)
# 2023.06.28: no
# notes: count each value, then walk from min to max writing each value
#        out as many times as it was counted
class Solution4:
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def counting_sort():
            # Create the counting hash map.
            counts = {}
            # Find the minimum and maximum values in the array.
            minVal, maxVal = min(nums), max(nums)
            # Update element's count in the hash map.
            for val in nums:
                counts[val] = counts.get(val, 0) + 1

            index = 0
            # Place each element in its correct position in the array.
            for val in range(minVal, maxVal + 1, 1):
                # Append all 'val's together if they exist.
                while counts.get(val, 0) > 0:
                    nums[index] = val
                    index += 1
                    counts[val] -= 1

        counting_sort()
        return nums


# Radix sort Approach
# Time: O(d(n+b))
# Space: O(n+b)
# 2023.06.28: no
# notes: a bit fiddly to write but easy to follow; bucket by each digit
#        from least to most significant, then split out negatives
class Solution5:
    # Radix sort function.
    def radix_sort(self, nums):
        # Find the absolute maximum element to find max number of digits.
        max_element = nums[0]
        for val in nums:
            max_element = max(abs(val), max_element)

        max_digits = 0
        while max_element > 0:
            max_digits += 1
            max_element = max_element // 10

        place_value = 1

        # Bucket sort function for each place value digit.
        def bucket_sort():
            buckets = [[] for i in range(10)]
            # Store the respective number based on it's digit.
            for val in nums:
                digit = abs(val) / place_value
                digit = int(digit % 10)
                buckets[digit].append(val)

            # Overwrite 'nums' in sorted order of current place digits.
            index = 0
            for digit in range(10):
                for val in buckets[digit]:
                    nums[index] = val
                    index += 1

        # Radix sort, least significant digit place to most significant.
        for _ in range(max_digits):
            bucket_sort()
            place_value *= 10

        # Seperate out negatives and reverse them.
        positives = [val for val in nums if val >= 0]
        negatives = [val for val in nums if val < 0]
        negatives.reverse()

        # Final 'arr' will be 'negative' elements, then 'positive' elements.
        return negatives + positives

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.radix_sort(nums)


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4(), Solution5()):
    assert sol.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert sol.sortArray([-2, 3, -5]) == [-5, -2, 3]
    assert sol.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
