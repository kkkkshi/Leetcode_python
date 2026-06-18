# 621. Task Scheduler

# Math
# Time: O(n)
# Space: O(1)
# 2023.07.20: yes
# notes: two cases. first, the most frequent task is large: count how
#        many tasks share that max frequency since they go at the end,
#        use (most_common_frequency-1) * (n+1) + most_common_elements.
#        otherwise the length itself is larger; take the max of the two
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        element_counts = Counter(tasks)
        most_common_frequency = element_counts.most_common(1)[0][1]
        most_common_elements = len([element for element, frequency in element_counts.items() if
                                frequency == most_common_frequency])
        if len(tasks) > (most_common_frequency-1) * (n+1) + most_common_elements:
            return len(tasks)
        else:
            return (most_common_frequency-1) * (n+1) + most_common_elements


# Greedy
# Time: O(n)
# Space: O(1)
# 2023.07.20: yes
# notes: see how much idle time is used; each step can fill at most
#        max_frequency-1 slots
class Solution2:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n

        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.leastInterval(["A","A","A","B","B","B"], 2) == 8
    assert sol.leastInterval(["A","A","A","B","B","B"], 0) == 6
    assert sol.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2) == 16
    assert sol.leastInterval(["A"], 5) == 1
