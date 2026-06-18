# 134. Gas Station

# Greedy One Pass
# Time: O(n)
# Space: O(1)
# notes: if total gas covers total cost a route exists; whenever the
#        running tank drops below 0, restart from the next station
class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)

        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1


# Tests:
for sol in (Solution(),):
    assert sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) == 3
    assert sol.canCompleteCircuit([2,3,4], [3,4,3]) == -1
    assert sol.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]) == 4
    assert sol.canCompleteCircuit([2], [2]) == 0
