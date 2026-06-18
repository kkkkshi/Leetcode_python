# 514. Freedom Trail

import collections


# Dynamic Programming 2D recursion
# Time: O(mn^2)
# Space: O(mn)
# 2023.07.26: no
# notes: i is the char now at 12:00, j is the index into key; try every
#        ring position for key[j] and take the cheapest rotation
class Solution:
    def findRotateSteps(self, ring, key):
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(key):
                return 0
            ans = float('inf')
            for k in range(len(ring)):
                if ring[k] == key[j]:
                    delta = abs(k - i)
                    steps = min(delta, len(ring) - delta)
                    ans = min(ans, steps + dp(k, j+1))
            memo[(i, j)] = ans
            return ans
        return dp(0, 0) + len(key)


# Dynamic Programming 1D Iteration
# Time: O(mn)
# Space: O(n)
# 2023.07.26: no
# notes: map each char to its ring positions, keep a 1D table, and for
#        every new char take the min over all previous positions, adding
#        min(clockwise, counter-clockwise) plus 1 for the press
class Solution2:
    def findRotateSteps(self, ring, key):
        indexes, n, dp, pre = collections.defaultdict(list), len(ring), [0] * len(ring), key[0]
        for i, c in enumerate(ring):
            indexes[c].append(i)
        for i in indexes[key[0]]:
            dp[i] = min(i, n - i) + 1
        for c in key[1:]:
            for i in indexes[c]:
                dp[i] = min(dp[j] + min(i - j, j + n - i) if i >= j else dp[j] + min(j - i, i + n - j) for j in indexes[pre]) + 1
            pre = c
        return min(dp[i] for i in indexes[key[-1]])


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.findRotateSteps("godding", "gd") == 4
    assert sol.findRotateSteps("godding", "godding") == 13
    assert sol.findRotateSteps("iotfo", "fio") == 8
    assert sol.findRotateSteps("edcba", "abcde") == 10
