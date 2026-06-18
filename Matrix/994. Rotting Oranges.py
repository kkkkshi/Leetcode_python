# 994. Rotting Oranges

# BFS Approach
# Time: O(nm)
# Space: O(nm)
# 2023.07.13: yes
# notes: multi-source BFS from rotten cells, using a (-1, -1) marker
#        to count elapsed minutes per level
from collections import deque


class Solution:
    def orangesRotting(self, grid):
        queue = deque()
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        queue.append((-1, -1))
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                minutes_elapsed += 1
                if queue:
                    queue.append((-1, -1))
            else:
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            queue.append((neighbor_row, neighbor_col))
        return minutes_elapsed if fresh_oranges == 0 else -1


# In-place BFS Approach
# Time: O(nm)
# Space: O(nm)
# 2023.07.13: yes
# notes: repeatedly sweep the grid, rotting neighbors of the current
#        timestamp; stop when no fresh orange gets infected
class Solution2:
    def orangesRotting(self, grid):
        ROWS, COLS = len(grid), len(grid[0])

        # run the rotting process, by marking the rotten oranges with the timestamp
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def runRottingProcess(timestamp):
            # flag to indicate if the rotting process should be continued
            to_be_continued = False
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == timestamp:
                        # current contaminated cell
                        for d in directions:
                            n_row, n_col = row + d[0], col + d[1]
                            if ROWS > n_row >= 0 and COLS > n_col >= 0:
                                if grid[n_row][n_col] == 1:
                                    # this fresh orange would be contaminated next
                                    grid[n_row][n_col] = timestamp + 1
                                    to_be_continued = True
            return to_be_continued
        timestamp = 2
        while runRottingProcess(timestamp):
            timestamp += 1
        # end of process, to check if there are still fresh oranges left
        for row in grid:
            for cell in row:
                if cell == 1:  # still got a fresh orange left
                    return -1
        # return elapsed minutes if no fresh orange left
        return timestamp - 2


# Tests:
def copy_grid(g):
    return [row[:] for row in g]


for sol in (Solution(), Solution2()):
    assert sol.orangesRotting(copy_grid([[2, 1, 1], [1, 1, 0], [0, 1, 1]])) == 4
    assert sol.orangesRotting(copy_grid([[2, 1, 1], [0, 1, 1], [1, 0, 1]])) == -1
    assert sol.orangesRotting(copy_grid([[0, 2]])) == 0
    assert sol.orangesRotting(copy_grid([[1]])) == -1
