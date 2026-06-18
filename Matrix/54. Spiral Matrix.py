# 54. Spiral Matrix

# Mark Visited Elements
# Time: O(mn)
# Space: O(1)
# 2023.06.20: yes
# notes: a bit over-engineered but the idea is the same; walk in
#        spiral order, marking visited cells until all four sides stall
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows, cols = len(matrix), len(matrix[0])
        visited = [[0] * (cols) for _ in range(rows)]
        visited[0][0] = 1
        result = [matrix[0][0]]
        check1, check2, check3, check4 = True, True, True, True
        i, j = 0, 0
        while True:
            while j+1 < cols and visited[i][j+1] == 0:
                j += 1
                visited[i][j] = 1
                result.append(matrix[i][j])
                check1 = False
            while i+1 < rows and visited[i+1][j] == 0:
                i += 1
                visited[i][j] = 1
                result.append(matrix[i][j])
                check2 = False
            while j-1 >= 0 and visited[i][j-1] == 0:
                j -= 1
                visited[i][j] = 1
                result.append(matrix[i][j])
                check3 = False
            while i-1 >= 0 and visited[i-1][j] == 0:
                i -= 1
                visited[i][j] = 1
                result.append(matrix[i][j])
                check4 = False
            if check1 and check2 and check3 and check4:
                return result
            check1, check2, check3, check4 = True, True, True, True


# Mark Visited In Place
# Time: O(mn)
# Space: O(1)
# notes: the reference answer; same idea, just cleaner; turn right
#        whenever the next cell is out of bounds or already visited
class Solution2:
    def spiralOrder(self, matrix):
        VISITED = 101
        rows, columns = len(matrix), len(matrix[0])
        # Four directions that we will move: right, down, left, up.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initial direction: moving right.
        current_direction = 0
        # The number of times we change the direction.
        change_direction = 0
        # Current place that we are at is (row, col).
        # row is the row index; col is the column index.
        row = col = 0
        # Store the first element and mark it as visited.
        result = [matrix[0][0]]
        matrix[0][0] = VISITED

        while change_direction < 2:

            while True:
                # Calculate the next place that we will move to.
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]

                # Break if the next step is out of bounds.
                if not (0 <= next_row < rows and 0 <= next_col < columns):
                    break
                # Break if the next step is on a visited cell.
                if matrix[next_row][next_col] == VISITED:
                    break

                # Reset this to 0 since we did not break and change the direction.
                change_direction = 0
                # Update our current position to the next step.
                row, col = next_row, next_col
                result.append(matrix[row][col])
                matrix[row][col] = VISITED

            # Change our direction.
            current_direction = (current_direction + 1) % 4
            # Increment change_direction because we changed our direction.
            change_direction += 1

        return result


# Set Up Boundaries
# Time: O(mn)
# Space: O(1)
# 2023.06.20: no
# notes: instead of marking visited cells, just shrink the four
#        boundaries inward as each side is consumed
class Solution3:
    def spiralOrder(self, matrix):
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Traverse from left to right.
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downwards.
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are now on a different row.
            if up != down:
                # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result


# Tests:
# Solution2 mutates the matrix, so give each solution a fresh copy.
for sol in (Solution(), Solution2(), Solution3()):
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert sol.spiralOrder(m1) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert sol.spiralOrder(m2) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    m3 = [[7]]
    assert sol.spiralOrder(m3) == [7]
    m4 = [[1, 2], [3, 4]]
    assert sol.spiralOrder(m4) == [1, 2, 4, 3]
