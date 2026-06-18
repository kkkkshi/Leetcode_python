# 1046. Last Stone Weight

import heapq
from bisect import insort
from typing import List


# Heap-Based Simulation (second best appraoch)
# Time: O(nlogn)
# Space: O(n)
# 2023.10.30: yes
# notes: max-heap of negated weights; pop the two heaviest, push back the
#        difference until at most one stone remains.
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x == y:
                continue
            else:
                heapq.heappush(stones, -x+y)
        return -stones[0] if len(stones) == 1 else 0


# Array-Based Simulation (not recommended)
# Time: O(n^2)
# Space: O(n)
# 2023.10.30: yes
# notes: repeatedly find and remove the two largest stones by scanning
#        the list, pushing back their difference.
class Solution2:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        :type stones: List[int]
        :rtype: int
        """
        def remove_largest():
            index_of_largest = stones.index(max(stones))
            # Swap the stone to be removed with the end.
            stones[index_of_largest], stones[-1] = stones[-1], stones[index_of_largest]
            return stones.pop()

        while len(stones) > 1:
            stone_1 = remove_largest()
            stone_2 = remove_largest()
            if stone_1 != stone_2:
                stones.append(stone_1 - stone_2)

        return stones[0] if stones else 0


# Sorted Array-Based Simulation (not recommended)
# Time: O(n^2)
# Space: O(n)
# 2023.10.30: yes
# notes: keep the list sorted, pop the two largest, and reinsert their
#        difference with bisect.
class Solution3:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        while len(stones) > 1:
            stone_1 = stones.pop()
            stone_2 = stones.pop()
            if stone_1 != stone_2:
                insort(stones, stone_1 - stone_2)
        return stones[0] if stones else 0


# Bucket Sort (best approach)
# Time: O(n+w)
# Space: O(w)
# 2023.10.30: yes
# notes: bucket-sort the weights by count. carry a biggest_weight; when it
#        is empty, the duplicates at a weight cancel in pairs (%2), leaving
#        at most one as biggest_weight. otherwise smash biggest_weight
#        against the current weight: if the remainder still fits within the
#        current weight, drop it back into the bucket and reset, else
#        shrink biggest_weight. two scans only, so 2n.
class Solution4:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        :type stones: List[int]
        :rtype: int
        """
        # Set up the bucket array.
        max_weight = max(stones)
        buckets = [0] * (max_weight + 1)

        # Bucket sort.
        for weight in stones:
            buckets[weight] += 1

        # Scan through the weights.
        biggest_weight = 0
        current_weight = max_weight
        while current_weight > 0:
            if buckets[current_weight] == 0:
                current_weight -= 1
            elif biggest_weight == 0:
                buckets[current_weight] %= 2
                if buckets[current_weight] == 1:
                    biggest_weight = current_weight
                current_weight -= 1
            else:
                buckets[current_weight] -= 1
                if biggest_weight - current_weight <= current_weight:
                    buckets[biggest_weight - current_weight] += 1
                    biggest_weight = 0
                else:
                    biggest_weight -= current_weight
        return biggest_weight


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.lastStoneWeight([2,7,4,1,8,1]) == 1
    assert sol.lastStoneWeight([1]) == 1
    assert sol.lastStoneWeight([2,2]) == 0
    assert sol.lastStoneWeight([3,7,2]) == 2
