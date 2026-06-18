# 45. Jump Game II

# Greedy
# Time: O(n)
# Space: O(1)
# 2023.07.29: yes
# notes: each jump, reach the farthest index possible; count a jump
#        whenever the current range is exhausted
class Solution:
    def jump(self, nums):
        # The starting range of the first jump is [0, 0]
        answer, n = 0, len(nums)
        cur_end, cur_far = 0, 0

        for i in range(n - 1):
            # Update the farthest reachable index of this jump.
            cur_far = max(cur_far, i + nums[i])

            # If we finish the starting range of this jump,
            # Move on to the starting range of the next jump.
            if i == cur_end:
                answer += 1
                cur_end = cur_far

        return answer


# Tests:
for sol in (Solution(),):
    assert sol.jump([2,3,0,1,4]) == 2
    assert sol.jump([2,3,1,1,4]) == 2
    assert sol.jump([0]) == 0
    assert sol.jump([1,2]) == 1
