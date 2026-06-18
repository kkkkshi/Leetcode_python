# 1197. Minimum Knight Moves

from collections import deque
from functools import lru_cache


# BFS Approach (best approach)
# Time: O((max(|x|, |y|))^2)
# Space: O((max(|x|, |y|))^2)
# 2023.07.11: yes
# notes: plain BFS from the origin, expanding level by level until
#        the target square is reached
class Solution:
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        def bfs(x, y):
            visited = set()
            queue = deque([(0, 0)])
            step = 0
            while queue:
                curr_level_cnt = len(queue)
                for i in range(curr_level_cnt):
                    cur_node_x, cur_node_y = queue.popleft()
                    if (cur_node_x, cur_node_y) == (x, y):
                        return step
                    for offset_x,offset_y in offsets:
                        new_node_x = cur_node_x + offset_x
                        new_node_y = cur_node_y + offset_y
                        if (new_node_x, new_node_y) not in visited:
                            visited.add((new_node_x, new_node_y))
                            queue.append((new_node_x, new_node_y))
                step += 1
        return bfs(x, y)


# Bidirectional BFS Approach
# Time: O((max(|x|, |y|))^2)
# Space: O((max(|x|, |y|))^2)
# 2023.07.11: no
# notes: search from origin toward target and from target toward
#        origin at the same time; they meet faster
class Solution2:
    def minKnightMoves(self, x: int, y: int) -> int:
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # the offsets in the eight directions
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        # data structures needed to move from the origin point
        origin_queue = deque([(0, 0, 0)])
        origin_distance = {(0, 0): 0}

        # data structures needed to move from the target point
        target_queue = deque([(x, y, 0)])
        target_distance = {(x, y): 0}

        while True:
            # check if we reach the circle of target
            origin_x, origin_y, origin_steps = origin_queue.popleft()
            if (origin_x, origin_y) in target_distance:
                return origin_steps + target_distance[(origin_x, origin_y)]

            # check if we reach the circle of origin
            target_x, target_y, target_steps = target_queue.popleft()
            if (target_x, target_y) in origin_distance:
                return target_steps + origin_distance[(target_x, target_y)]

            for offset_x, offset_y in offsets:
                # expand the circle of origin
                next_origin_x, next_origin_y = origin_x + offset_x, origin_y + offset_y
                if (next_origin_x, next_origin_y) not in origin_distance:
                    origin_queue.append((next_origin_x, next_origin_y, origin_steps + 1))
                    origin_distance[(next_origin_x, next_origin_y)] = origin_steps + 1

                # expand the circle of target
                next_target_x, next_target_y = target_x + offset_x, target_y + offset_y
                if (next_target_x, next_target_y) not in target_distance:
                    target_queue.append((next_target_x, next_target_y, target_steps + 1))
                    target_distance[(next_target_x, next_target_y)] = target_steps + 1


# DFS (Depth-First Search) with Memoization Approach
# Time: O((max(|x|, |y|))^2)
# Space: O((max(|x|, |y|))^2)
# 2023.07.11: no
# notes: by symmetry only one quadrant matters, so fold x,y to abs
#        values and recurse on (x-1,y-2) and (x-2,y-1); base cases
#        are x+y==0 -> 0 and x+y==2 -> 2
class Solution3:
    def minKnightMoves(self, x: int, y: int) -> int:
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        @lru_cache(maxsize=None)
        def dfs(x, y):
            if x + y == 0:
                # base case: (0, 0)
                return 0
            elif x + y == 2:
                # base case: (1, 1), (0, 2), (2, 0)
                return 2
            else:
                return min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1
        return dfs(abs(x), abs(y))


# Tests:
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.minKnightMoves(0, 0) == 0
    assert sol.minKnightMoves(2, 1) == 1
    assert sol.minKnightMoves(5, 5) == 4
