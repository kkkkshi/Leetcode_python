# 36. Valid Sudoku

from typing import List


# Hash Set
# Time: O(n^2)
# Space: O(n^2)
# 2023.10.08: yes
# notes: track seen digits per row, column and box with sets
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])
                pos = i // 3 * 3 + j // 3
                if board[i][j] in boxes[pos]:
                    return False
                boxes[pos].add(board[i][j])
        return True


# Array of Fixed Length
# Time: O(n^2)
# Space: O(n^2)
# 2023.10.08: yes
# notes: same idea but mark seen digits in fixed length arrays
class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        N = 9

        # Use an array to record the status
        rows = [[0] * N for _ in range(N)]
        cols = [[0] * N for _ in range(N)]
        boxes = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                # Check if the position is filled with number
                if board[r][c] == ".":
                    continue

                pos = int(board[r][c]) - 1

                # Check the row
                if rows[r][pos] == 1:
                    return False
                rows[r][pos] = 1

                # Check the column
                if cols[c][pos] == 1:
                    return False
                cols[c][pos] = 1

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if boxes[idx][pos] == 1:
                    return False
                boxes[idx][pos] = 1

        return True


# Bitmasking
# Time: O(n^2)
# Space: O(n)
# 2023.10.08: no
# notes: store each digit as a bit to save space
class Solution3:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        N = 9
        # Use binary number to check previous occurrence
        rows = [0] * N
        cols = [0] * N
        boxes = [0] * N

        for r in range(N):
            for c in range(N):
                # Check if the position is filled with number
                if board[r][c] == ".":
                    continue

                pos = int(board[r][c]) - 1

                # Check the row
                if rows[r] & (1 << pos):
                    return False
                rows[r] |= (1 << pos)

                # Check the column
                if cols[c] & (1 << pos):
                    return False
                cols[c] |= (1 << pos)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if boxes[idx] & (1 << pos):
                    return False
                boxes[idx] |= (1 << pos)

        return True


# Tests:
valid_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
invalid_board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.isValidSudoku(valid_board) is True
    assert sol.isValidSudoku(invalid_board) is False
