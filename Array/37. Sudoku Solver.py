# 37. Sudoku Solver

# Backtrack
# Time: O((9!)^9)
# Space: O(81)
# 2023.08.03: yes
# notes: at first not sure how to check whether a cell is in one small
#        block; board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3] == n
#        is a clever way. the rest is plain backtracking.
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None
        """
        def backtrack(board, i, j):
            def isValid(board, r, c, n):
                for i in range(9):
                    if board[r][i] == n:
                        return False
                    if board[i][c] == n:
                        return False
                    if board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3] == n:
                        return False
                return True
            m, n = 9, 9
            if j == n:
                # reached last column, move to next row from start
                return backtrack(board, i + 1, 0)
            if i == m:
                # found a valid solution, trigger base case
                return True

            if board[i][j] != '.':
                # preset number, no need to enumerate
                return backtrack(board, i, j + 1)

            for ch in range(ord('1'), ord('9') + 1):
                ch = chr(ch)
                # skip an invalid number
                if not isValid(board, i, j, ch):
                    continue

                board[i][j] = ch
                # found a valid solution, return immediately
                if backtrack(board, i, j + 1):
                    return True
                board[i][j] = '.'
                # tried 1~9 with no solution, dead end
            return False
        return backtrack(board, 0, 0)


# Tests:
for sol in (Solution(),):
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    sol.solveSudoku(board)
    expected = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
    assert board == expected
