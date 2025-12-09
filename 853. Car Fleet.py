# Array
# Time: O(n)
# Space: O(n)
# 2023.10.08: no
# notes: 根据position排序，然后计算需要多少秒到终点，如果比前面一个少，那就fleet
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


# Test
test = Solution()
test.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])