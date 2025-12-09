# Heap-Based Simulation (second best appraoch)
# Time: O(nlogn)
# Space: O(n)
# 2023.10.30: yes
import heapq
from bisect import bisect
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
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
class Solution2:
    def lastStoneWeight(self, stones: List[int]) -> int:

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
class Solution3:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            stone_1 = stones.pop()
            stone_2 = stones.pop()
            if stone_1 != stone_2:
                bisect.insort(stones, stone_1 - stone_2)
        return stones[0] if stones else 0

# Bucket Sort (best approach)
# Time: O(n+w)
# Space: O(w)
# 2023.10.30: yes
# notes: 这个桶排序有点抽象，先把数字根据桶排序好，确定最大值，有两个变量，biggest_weight和current_weight，
# 如果biggest_weight是空的话，就可以%2消除多的部分，最后没有多的话，直接降低下一个值，有多的话，就biggest_weight变成这个值
# 然后降低成下一个值，取减下一个值，如果够减两倍，那就继续保留biggest_weight,如果不够减两倍，就biggest-current然后存
# 到bucket里面去，直到运行到n = 1位置，其实只需要遍历两遍即可，所以是2n
class Solution4:
    def lastStoneWeight(self, stones: List[int]) -> int:

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


# Test:
test = Solution4()
test.lastStoneWeight([2,7,4,1,8,1])
test.lastStoneWeight([1])
