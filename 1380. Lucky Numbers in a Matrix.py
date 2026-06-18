# 1380. Lucky Numbers in a Matrix

# Recursion
# Time: O(mn)
# Space: O(1)
# 2023.08.14: no
# notes: a matrix has at most one lucky number, so take the max of
#        each row's min and the min of each col's max and compare
# 1. a matrix cannot hold two lucky numbers
# 2. find max of row mins and min of col maxes, lucky if they match
import math


class Solution:
    def luckyNumbers(self, matrix):
        # max of row min
        maxMin = -math.inf
        # min of max col
        minMax = math.inf
        for row in range(len(matrix)):
            maxMin = max(maxMin, min(matrix[row]))
        for col in zip(*matrix):
            minMax = min(minMax, max(col))
        return [maxMin] if maxMin == minMax else []


# Tests:
for sol in (Solution(),):
    assert sol.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]) == [15]
    assert sol.luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7],
                             [15, 16, 17, 12]]) == [12]
    assert sol.luckyNumbers([[7, 8], [1, 2]]) == [7]
