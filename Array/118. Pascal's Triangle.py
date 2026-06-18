# 118. Pascal's Triangle

from typing import List


# Level Order Traversal Approach
# Time: O(n^2)
# Space: O(1)
# 2023.09.10: yes
# notes: build each row from the previous one, summing adjacent
#        pairs and padding 1 on both ends
class Solution:
    def nextrow(self, lsts):
        cur_row = [1]
        for i in range(len(lsts)-1):
            cur_row.append(lsts[i]+lsts[i+1])
        cur_row.append(1)
        return cur_row

    def generate(self, numRows: int) -> List[List[int]]:
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        results = []
        if numRows > 0:
            results.append([1])
        if numRows > 1:
            results.append([1,1])
        count = 2
        while count < numRows:
            results.append(self.nextrow(results[-1]))
            count += 1
        return results


# Level Order Traversal Approach
# Time: O(n^2)
# Space: O(1)
# 2023.09.10: yes
# notes: same row-building idea as the approach above
class Solution2:
    def generate(self, num_rows: int) -> List[List[int]]:
        """
        :type num_rows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.generate(1) == [[1]]
    assert sol.generate(2) == [[1], [1, 1]]
    assert sol.generate(5) == [[1], [1, 1], [1, 2, 1],
                               [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert sol.generate(0) == []
