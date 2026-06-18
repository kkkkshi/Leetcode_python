# 542. 01 Matrix

# DFS Approach (best approach)
# Time: O(mn)
# Space: O(mn)
# 2023.07.13: yes
# notes: push all zeros into a queue, then BFS outward, relaxing
#        each neighbor distance like multi-source shortest path
from collections import deque


class Solution:
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(mat), len(mat[0])
        results = [[float("inf")] * col for _ in range(row)]
        offsets = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    q.append([i, j])
                    results[i][j] = 0
        while len(q) != 0:
            cur_row, cur_col = q.popleft()
            for i in range(len(offsets)):
                next_row, next_col = cur_row+offsets[i][0], cur_col+offsets[i][1]
                if next_row < 0 or next_row >= row or next_col < 0 or next_col >= col:
                    continue
                if results[cur_row][cur_col]+1 < results[next_row][next_col]:
                    results[next_row][next_col] = results[cur_row][cur_col]+1
                    q.append([next_row, next_col])
        return results


# Dynamic Programming (best approach)
# Time: O(mn)
# Space: O(mn)
# 2023.07.13: yes
# notes: two passes, first from top-left then bottom-right, each
#        cell takes the smaller neighbor distance plus one
class Solution2:
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        dp = [row[:] for row in mat]
        m, n = len(dp), len(dp[0])
        for row in range(m):
            for col in range(n):
                min_neighbor = float("inf")
                if dp[row][col] != 0:
                    if row > 0:
                        min_neighbor = min(min_neighbor, dp[row - 1][col])
                    if col > 0:
                        min_neighbor = min(min_neighbor, dp[row][col - 1])
                    dp[row][col] = min_neighbor + 1
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                min_neighbor = float("inf")
                if dp[row][col] != 0:
                    if row < m - 1:
                        min_neighbor = min(min_neighbor, dp[row + 1][col])
                    if col < n - 1:
                        min_neighbor = min(min_neighbor, dp[row][col + 1])
                    dp[row][col] = min(dp[row][col], min_neighbor + 1)
        return dp


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == \
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert sol.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == \
        [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    assert sol.updateMatrix([[0]]) == [[0]]
    assert sol.updateMatrix([[0, 1, 1]]) == [[0, 1, 2]]
