# Greedy using Heap
# Time: O(nlogn)
# Space: O(n)
# 2023.09.13: no
# notes: 循环每一个element，并且把他们的top element 存到Heap上，如果断层了，并且array的长度小于3，证明无解
# greedy, 1. 如果能加后面，就加后面， 2. 不能就新建一个array，3. 遍历完之后检查所有heap里的范围, [start, end]
import heapq
class Solution:
    def isPossible(self, nums):
        subsequences = []

        for num in nums:
            # Condition 1 - remove non-qualifying subsequences
            while subsequences and subsequences[0][1] + 1 < num:
                current_subsequence = heapq.heappop(subsequences)
                subsequence_length = current_subsequence[1] - current_subsequence[0] + 1
                if subsequence_length < 3:
                    return False

            # Condition 2 - create a new subsequence
            if not subsequences or subsequences[0][1] == num:
                heapq.heappush(subsequences, [num, num])
            else:
                # Condition 3 - add num to an existing subsequence
                current_subsequence = heapq.heappop(subsequences)
                heapq.heappush(subsequences, [current_subsequence[0], num])

        # If any subsequence is of length less than 3, return False
        while subsequences:
            current_subsequence = heapq.heappop(subsequences)
            subsequence_length = current_subsequence[1] - current_subsequence[0] + 1
            if subsequence_length < 3:
                return False

        return True


# Greedy using Maps
# Time: O(n)
# Space: O(n)
# 2023.09.13: no
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
from typing import List
class Solution5:
    def isPossible(self, nums: List[int]) -> bool:
        # 使用字典统计 nums 中元素的频率
        freq, need = {}, {}
        for v in nums:
            freq[v] = freq.get(v, 0) + 1

        for v in nums:
            if freq[v] == 0:
                # 已经被用到其他子序列中
                continue
            if v in need and need[v] > 0:
                # v 可以接到之前的某个序列后面
                freq[v] -= 1
                need[v] -= 1
                need[v + 1] = need.get(v + 1, 0) + 1
            elif freq[v] > 0 and freq.get(v + 1, 0) > 0 and freq.get(v + 2, 0) > 0:
                # 将 v 作为开头，新建一个长度为 3 的子序列 [v,v+1,v+2]
                freq[v] -= 1
                freq[v + 1] -= 1
                freq[v + 2] -= 1
                need[v + 3] = need.get(v + 3, 0) + 1
            else:
                # 两种情况都不符合，则无法分配
                return False

        return True


test = Solution2()
test.isPossible([1,2,3,4,4,5])
test.isPossible([1,2,3,3,4,4,5,5])
test.isPossible([1,2,3,4,5])
test.isPossible([1,2,3,4,4,5])
