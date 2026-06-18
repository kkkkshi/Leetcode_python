# 49. Group Anagrams

# Categorize by Count (best approach)
# Time: O(nk)
# Space: O(nk)
# 2023.06.23: yes
# notes: key each string by its 26-letter count tuple and group
import collections


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        results = {}
        for s in strs:
            new_array = [0] * 26
            for i in s:
                new_array[ord(i) - ord('a')] += 1
            if tuple(new_array) not in results:
                results[tuple(new_array)] = [s]
            else:
                results[tuple(new_array)].append(s)
        return results.values()


# Categorize by Sorted String Approach
# Time: O(nk)
# Space: O(nk)
# 2023.06.23: yes
# notes: key each string by its sorted characters and group
class Solution2:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


# Tests:
def normalize(groups):
    return sorted(sorted(g) for g in groups)


for sol in (Solution(), Solution2()):
    assert normalize(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == \
        [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert normalize(sol.groupAnagrams([""])) == [[""]]
    assert normalize(sol.groupAnagrams(["a"])) == [["a"]]
