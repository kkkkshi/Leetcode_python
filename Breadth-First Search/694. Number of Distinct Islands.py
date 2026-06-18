# 694. Number of Distinct Islands

# Hash By Path Signature
# Time: O(mn)
# Space: O(mn)
# 2023.08.03: yes
# notes: record the dfs path of each island so identical shapes hash the
#        same; append a marker when entering and when leaving a cell to
#        keep distinct shapes apart
class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(grid, i, j, cur):
            m, n = len(grid), len(grid[0])
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] == 0:
                return

            grid[i][j] = 0
            path.append(cur)
            dfs(grid, i + 1, j, "A")
            dfs(grid, i, j + 1, "B")
            dfs(grid, i - 1, j, "C")
            dfs(grid, i, j - 1, "D")
            path.append("0")

        diff_island = set()
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    path = []
                    dfs(grid, i, j, "0")
                    diff_island.add("".join(path))
        return len(diff_island)


# Brute Force:
# Time: O(m^2n^2)
# Space: O(mn)
# 2023.08.03: yes
# notes: store every island's cells, compare by length then cell by cell;
#        slow when many islands share the same size
class Solution2:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def current_island_is_unique():
            for other_island in unique_islands:
                if len(other_island) != len(current_island):
                    continue
                for cell_1, cell_2 in zip(current_island, other_island):
                    if cell_1 != cell_2:
                        break
                else:
                    return False
            return True

        # Do a DFS to find all cells in the current island.
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if (row, col) in seen or not grid[row][col]:
                return
            seen.add((row, col))
            current_island.append((row - row_origin, col - col_origin))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Repeatedly start DFS's as long as there are islands remaining.
        seen = set()
        unique_islands = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_island = []
                row_origin = row
                col_origin = col
                dfs(row, col)
                if not current_island or not current_island_is_unique():
                    continue
                unique_islands.append(current_island)
        return len(unique_islands)


# Hash By Local Coordinates
# Time: O(mn)
# Space: O(mn)
# 2023.08.03: yes
# notes: record each cell offset from the island's origin; two islands
#        with the same set of offsets are the same shape
class Solution3:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # Do a DFS to find all cells in the current island.
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if (row, col) in seen or not grid[row][col]:
                return
            seen.add((row, col))
            current_island.add((row - row_origin, col - col_origin))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Repeatedly start DFS's as long as there are islands remaining.
        seen = set()
        unique_islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_island = set()
                row_origin = row
                col_origin = col
                dfs(row, col)
                if current_island:
                    unique_islands.add(frozenset(current_island))

        return len(unique_islands)


# Tests:
for Sol in (Solution, Solution2, Solution3):
    sol = Sol()
    assert sol.numDistinctIslands(
        [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]) == 1
    assert sol.numDistinctIslands(
        [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]) == 3
    assert sol.numDistinctIslands([[0, 0, 0], [0, 0, 0]]) == 0
