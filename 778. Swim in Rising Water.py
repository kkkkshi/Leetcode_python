# 778. Swim in Rising Water

# Bineary Search + DFS
# Time: O(n^2 log n)
# Space: O(n^2)
# 2023.11.01: yes
# notes: binary search the time t; for each t run DFS to check if the
#        bottom-right is reachable using only cells with height <= t
class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        def canReach(t):
            if grid[0][0] > t:
                return False
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            stack = [(0, 0)]
            while stack:
                x, y = stack.pop()
                if x == n - 1 and y == n - 1:
                    return True
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] <= t:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
            return False

        lo, hi = 0, n * n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if canReach(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


# Tests:
for sol in (Solution(),):
    assert sol.swimInWater([[0, 2], [1, 3]]) == 3
    assert sol.swimInWater(
        [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16],
         [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]) == 16
    assert sol.swimInWater([[0]]) == 0
    assert sol.swimInWater([[3, 2], [0, 1]]) == 3
