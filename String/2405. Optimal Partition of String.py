# 2405. Optimal Partition of String

# Greedy
# Time: O(n)
# Space: O(1)
# 2023.08.17: yes
# notes: keep extending the current substring; on a repeat char start
#        a new substring and count one more partition
class Solution:
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        saving = []
        res = 0
        for i in s:
            if i not in saving:
                saving.append(i)
            else:
                res += 1
                saving = [i]
        return res+1


# Tests:
for sol in (Solution(),):
    assert sol.partitionString("abacaba") == 4
    assert sol.partitionString("ssssss") == 6
    assert sol.partitionString("abc") == 1
    assert sol.partitionString("a") == 1
