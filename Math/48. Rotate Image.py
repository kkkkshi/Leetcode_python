# 48. Rotate Image

# Reverse on Diagonal and then Reverse Left to Right
# Time: O(m)
# Space: O(1)
# 2023.06.19: no
# notes: transpose to swap rows and columns, then reverse each
#        row; hard to see but easy to write once you do
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            x, y = 0, len(row)-1
            while x < y:
                row[x], row[y] = row[y], row[x]
                x += 1
                y -= 1


# Rotate Groups of Four Cells
# Time: O(m)
# Space: O(1)
# notes: rotate four cells at once, not two; easy to get the
#        index math wrong here
class Solution2:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp


# Tests:
for sol in (Solution(), Solution2()):
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(a)
    assert a == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    b = [[1, 2], [3, 4]]
    sol.rotate(b)
    assert b == [[3, 1], [4, 2]]
    c = [[1]]
    sol.rotate(c)
    assert c == [[1]]
