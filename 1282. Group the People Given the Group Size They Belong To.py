# Hashmap
# Time: O(n)
# Space: O(n)
# 2023.09.11: yes
# notes: O(n)是O(n)但是真的很蠢。。。不过算是熟悉了一下dictionary的写法吧。。。
from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
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
# notes: 很棒的方法
class Solution2:
    def groupThePeople(self, groupSizes):
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


# Tests:
test = Solution2()
test.groupThePeople(groupSizes = [3,3,3,3,3,1,3])