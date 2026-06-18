# 1282. Group the People Given the Group Size They Belong To

from typing import List


# Hashmap
# Time: O(n)
# Space: O(n)
# 2023.09.11: yes
# notes: O(n) but pretty clunky; mostly a refresher on dictionary
#        usage, bucket indices by size then chunk each bucket
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        results = []
        saving = {}
        for i,n in enumerate(groupSizes):
            if n not in saving:
                saving[n] = [i]
            else:
                saving[n].append(i)
        tmp = []
        for key, value in saving.items():
            while value:
                count = key
                while count:
                    tmp.append(value[-1])
                    value.pop()
                    count -= 1
                results.append(tmp)
                tmp = []
        return results


# Greedy
# Time: O(n)
# Space: O(n)
# 2023.09.11: no
# notes: nice approach
class Solution2:
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        # A list of lists to store indices based on group size.
        sz_to_group = [[] for _ in range(len(groupSizes) + 1)]

        for i in range(len(groupSizes)):
            sz_to_group[groupSizes[i]].append(i)

            # When the list size equals the group size, empty it and store it in the answer.
            if len(sz_to_group[groupSizes[i]]) == groupSizes[i]:
                ans.append(sz_to_group[groupSizes[i]])
                sz_to_group[groupSizes[i]] = []

        return ans


def normalize(groups):
    # order-independent view: sort each group and the list of groups
    return sorted(sorted(g) for g in groups)


def valid(groups, group_sizes):
    # every person appears once and each group has the wanted size
    seen = sorted(p for g in groups for p in g)
    if seen != list(range(len(group_sizes))):
        return False
    return all(len(g) == group_sizes[g[0]] for g in groups)


# Tests:
for sol in (Solution(), Solution2()):
    res = sol.groupThePeople([3, 3, 3, 3, 3, 1, 3])
    assert valid(res, [3, 3, 3, 3, 3, 1, 3]) is True
    res = sol.groupThePeople([2, 1, 3, 3, 3, 2])
    assert valid(res, [2, 1, 3, 3, 3, 2]) is True
    assert normalize(sol.groupThePeople([1, 1, 1])) == [[0], [1], [2]]
