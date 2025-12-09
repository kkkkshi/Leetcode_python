# Breadth First Search
# Time: O(nlogn)
# Space: O(1)
# 2023.10.31: yes
import heapq
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        h = []
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        rows, cols = len(rooms), len(rooms[0])
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    heapq.heappush(h, (i, j))
        while h:
            cur_row, cur_col = heapq.heappop(h)
            cur_value = rooms[cur_row][cur_col]
            for i in directions:
                next_row, next_col = cur_row + i[0], cur_col + i[1]
                if (
                    next_row < rows
                    and next_row >= 0
                    and next_col < cols
                    and next_col >= 0
                ):
                    if rooms[next_row][next_col] > cur_value + 1:
                        rooms[next_row][next_col] = cur_value + 1
                        heapq.heappush(h, (next_row, next_col))
        return rooms


# Tests:
test = Solution()
test.wallsAndGates(
    [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
)

test.wallsAndGates([[-1]])