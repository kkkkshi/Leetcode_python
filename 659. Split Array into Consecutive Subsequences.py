# 659. Split Array into Consecutive Subsequences

# Greedy using Heap
# Time: O(nlogn)
# Space: O(n)
# 2023.09.13: no
# notes: keep each run on a heap keyed by [end, length]; for each num
#        drop finished runs that are too short, then either extend the
#        run ending at num-1 or start a new run [num, length 1]
import heapq
class Solution:
    def isPossible(self, nums):
        # each entry is [end, length]
        subsequences = []

        for num in nums:
            # Condition 1 - remove non-qualifying subsequences
            while subsequences and subsequences[0][0] + 1 < num:
                current_subsequence = heapq.heappop(subsequences)
                subsequence_length = current_subsequence[1]
                if subsequence_length < 3:
                    return False

            # Condition 2 - create a new subsequence
            if not subsequences or subsequences[0][0] == num:
                heapq.heappush(subsequences, [num, 1])
            else:
                # Condition 3 - add num to an existing subsequence
                current_subsequence = heapq.heappop(subsequences)
                heapq.heappush(subsequences, [num, current_subsequence[1] + 1])

        # If any subsequence is of length less than 3, return False
        while subsequences:
            current_subsequence = heapq.heappop(subsequences)
            subsequence_length = current_subsequence[1]
            if subsequence_length < 3:
                return False

        return True


# Greedy using Maps
# Time: O(n)
# Space: O(n)
# 2023.09.13: no
# notes: extend an existing run ending at num-1 when possible, else try
#        to start a new run num,num+1,num+2 using remaining frequencies
class Solution2:
    def isPossible(self, nums):
        subsequences = {}
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        for num in nums:
            # num already part of a valid subsequence.
            if frequency[num] == 0:
                continue

            # If a valid subsequence exists with the last element = num - 1.
            if num - 1 in subsequences and subsequences[num - 1] > 0:
                subsequences[num - 1] -= 1
                subsequences[num] = subsequences.get(num, 0) + 1

            elif num + 1 in frequency and num + 2 in frequency and frequency[num + 1] > 0 and frequency[num + 2] > 0:
                # If we want to start a new subsequence, check if num + 1 and num + 2 exist.
                # Update the list of subsequences with the newly created subsequence.
                subsequences[num + 2] = subsequences.get(num + 2, 0) + 1
                frequency[num + 1] -= 1
                frequency[num + 2] -= 1

            else:
                # No valid subsequence is possible with num.
                return False

            frequency[num] -= 1

        return True


# Dynamic Programming
# Optimal Space
# notes: freq counts remaining numbers; need[v] counts runs waiting for v.
#        append v to a waiting run, else open a new run [v,v+1,v+2]
from typing import List
class Solution5:
    def isPossible(self, nums: List[int]) -> bool:
        # count the frequency of each value in nums
        freq, need = {}, {}
        for v in nums:
            freq[v] = freq.get(v, 0) + 1

        for v in nums:
            if freq[v] == 0:
                # already used by another subsequence
                continue
            if v in need and need[v] > 0:
                # v can extend a previous subsequence
                freq[v] -= 1
                need[v] -= 1
                need[v + 1] = need.get(v + 1, 0) + 1
            elif freq[v] > 0 and freq.get(v + 1, 0) > 0 and freq.get(v + 2, 0) > 0:
                # start a new length-3 subsequence [v,v+1,v+2] with v as head
                freq[v] -= 1
                freq[v + 1] -= 1
                freq[v + 2] -= 1
                need[v + 3] = need.get(v + 3, 0) + 1
            else:
                # neither case works, cannot split
                return False

        return True


# Tests:
for sol in (Solution(), Solution2(), Solution5()):
    assert sol.isPossible([1, 2, 3, 4, 4, 5]) is False
    assert sol.isPossible([1, 2, 3, 3, 4, 4, 5, 5]) is True
    assert sol.isPossible([1, 2, 3, 4, 5]) is True
    assert sol.isPossible([1, 2, 3, 3, 4, 5]) is True
    assert sol.isPossible([1, 2]) is False
