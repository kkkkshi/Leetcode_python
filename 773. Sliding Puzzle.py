# 773. Sliding Puzzle

import collections
import heapq


# Breadth First Search
# Time: O(mn)
# Space: O(1)
# 2023.07.31: no
# notes: encode the 2*3 board as a length-6 string for easy mapping;
#        the 0 can move up/down/left/right (+-1 or +-width). Run
#        level-order BFS over states, count steps until "123450";
#        if every state is exhausted the board has no solution
class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        s = "".join(str(d) for row in board for d in row)
        dq, seen = collections.deque(), {s}
        dq.append((s, s.index("0")))
        steps, height, width = 0, len(board), len(board[0])
        while dq:
            for _ in range(len(dq)):
                t, i = dq.popleft()
                if t == "123450":
                    return steps
                x, y = i // width, i % width
                for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                    if height > r >= 0 <= c < width:
                        ch = [d for d in t]
                        ch[i], ch[r * width + c] = ch[r * width + c], "0"
                        s = "".join(ch)
                        if s not in seen:
                            seen.add(s)
                            dq.append((s, r * width + c))
            steps += 1
        return -1


# A* Search
# Time: O(mn)
# Space: O(1)
# 2023.07.31: no
# notes: upgraded Dijkstra; priority = steps so far + heuristic, where
#        the heuristic is the total Manhattan distance of each tile
#        from its goal cell. Push states with smaller cost first
class Solution2:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        goal = [[1, 2, 3], [4, 5, 0]]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        def heuristic(board):
            count = 0
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] != 0:
                        x, y = int((board[i][j] - 0.1) / 3), (board[i][j] - 1) % 3
                        count += abs(x - i) + abs(y - j)
            return count

        def a_star(start):
            q = []
            heapq.heappush(q, (0, start))
            cost = {}
            cost[str(start)] = 0

            while q:
                board_now = heapq.heappop(q)[1]
                if heuristic(board_now) == 0:
                    break
                i, j = 0, 0
                for i in range(len(board_now)):
                    for j in range(len(board_now[i])):
                        if board_now[i][j] == 0:
                            break
                    if board_now[i][j] == 0:
                        break

                for directions in range(4):
                    nx = i + dx[directions]
                    ny = j + dy[directions]
                    if (
                        nx < len(board_now)
                        and nx >= 0
                        and ny >= 0
                        and ny < len(board_now[0])
                    ):
                        board_next = [[0] * 3, [0] * 3]
                        board_next[0][:] = board_now[0]
                        board_next[1][:] = board_now[1]
                        board_next[i][j] = board_next[nx][ny]
                        board_next[nx][ny] = 0
                        if (
                            str(board_next) not in cost
                            or cost[str(board_now)] + 1 < cost[str(board_next)]
                        ):
                            cost[str(board_next)] = cost[str(board_now)] + 1
                            priority = cost[str(board_now)] + 1 + heuristic(board_next)
                            heapq.heappush(q, (priority, board_next))
            if str(goal) in cost:
                return cost[str(goal)]
            return -1

        return a_star(board)


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.slidingPuzzle([[1, 2, 3], [4, 0, 5]]) == 1
    assert sol.slidingPuzzle([[1, 2, 3], [5, 4, 0]]) == -1
    assert sol.slidingPuzzle([[4, 1, 2], [5, 0, 3]]) == 5
    assert sol.slidingPuzzle([[1, 2, 3], [4, 5, 0]]) == 0
