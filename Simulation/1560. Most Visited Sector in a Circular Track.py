# 1560. Most Visited Sector in a Circular Track

# Loop Approach
# Time: O(n)
# Space: O(n)
# 2023.07.22: yes
# notes: only the first and last sector matter; the most visited
#        sectors are the arc from rounds[0] to rounds[-1]
class Solution:
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        start, end = rounds[0], rounds[-1]
        if start <= end:
            return list(range(start, end + 1))
        return list(range(1, end + 1)) + list(range(start, n + 1))


# Tests:
for sol in (Solution(),):
    assert sol.mostVisited(4, [1, 3, 1, 2]) == [1, 2]
    assert sol.mostVisited(2, [2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2]
    assert sol.mostVisited(7, [1, 3, 5, 7]) == [1, 2, 3, 4, 5, 6, 7]
