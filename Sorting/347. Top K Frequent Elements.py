# 347. Top K Frequent Elements

import heapq
from collections import Counter
import random


# Heap Approach
# Time: O(nlogk)
# Space: O(n+k)
# 2023.06.23: yes
# notes: count frequencies, sort by count and take the top k
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        results = []
        counts = Counter(nums)
        sorted_counter = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            results.append(sorted_counter[i][0])
        return results


# Heap Approach
# Time: O(nlogk)
# Space: O(n+k)
# 2023.06.23: yes
# notes: more concise using heapq.nlargest
class Solution2:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # O(1) time
        if k == len(nums):
            return nums

        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)


# Quickselect (Hoare's selection algorithm) (best approach)
# Time: O(n)
# Space: O(n+)
# 2023.06.23: no
# notes: only the top k matter and their order does not, so
#        quickselect partitions until the kth boundary is placed
class Solution3:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place.
            """
            # base case: the list contains only one element
            if left == right:
                return

            # select a random pivot_index
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return
                # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array.
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sorted(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sorted(sol.topKFrequent([1], 1)) == [1]
    assert sorted(sol.topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3, 5, 1], 3)) == [1, 2, 3]
