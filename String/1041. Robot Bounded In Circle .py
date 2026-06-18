# 1041. Robot Bounded In Circle

# Math
# Time: O(n)
# Space: O(1)
# 2023.08.18: no
# notes: after one pass the robot is bounded if it returns to the origin
#        or it no longer faces north; then the cycle repeats and stays
#        within a circle.
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        :type instructions: str
        :rtype: bool
        """
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x = y = 0
        idx = 0
        for i in instructions:
            if i == "L":
                idx = (idx + 3) % 4
            elif i == "R":
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]
        return (x == 0 and y == 0) or idx != 0


# Tests:
for sol in (Solution(),):
    assert sol.isRobotBounded("GGLLGG") == True
    assert sol.isRobotBounded("GG") == False
    assert sol.isRobotBounded("GL") == True
    assert sol.isRobotBounded("GGGLGLGLGG") == True
