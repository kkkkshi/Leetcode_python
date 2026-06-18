# 74. Search a 2D Matrix

# Binary Search
# Time: O(n)
# Space: O(n)
# 2023.10.08: no
# notes: still binary search, just map a flat index to a cell with
#        pivot_idx // n for the row and pivot_idx % n for the col
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # binary search
        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False


# Tests:
for sol in (Solution(),):
    assert sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) is True
    assert sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) is False
    assert sol.searchMatrix([[1]], 1) is True
    assert sol.searchMatrix([[1]], 2) is False
