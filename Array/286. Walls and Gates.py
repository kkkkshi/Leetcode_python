# 286. Walls and Gates

# Breadth First Search
# Time: O(nlogn)
# Space: O(1)
# 2023.10.31: yes
# notes: push every gate into a heap, then relax neighbours by one
#        whenever a shorter distance is found
import heapq
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
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
INF = 2147483647
for sol in (Solution(),):
    grid = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]
    sol.wallsAndGates(grid)
    assert grid == [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]

    single = [[-1]]
    sol.wallsAndGates(single)
    assert single == [[-1]]
