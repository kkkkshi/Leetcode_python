# 853. Car Fleet

# Array
# Time: O(n)
# Space: O(n)
# 2023.10.08: no
# notes: sort by position, compute each car's time to the target; going
#        from the back, a car forms a new fleet only if it is slower
#        than the fleet ahead, otherwise it merges into it.
class Solution:
    def carFleet(self, target, pos, speed):
        new_array = sorted(zip(pos, speed))
        time = [float(target - p) / s for p, s in new_array]
        res = cur = 0
        for t in time[::-1]:
            if t > cur:
                res += 1
                cur = t
        return res


# Tests:
for sol in (Solution(),):
    assert sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert sol.carFleet(10, [3], [3]) == 1
    assert sol.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
