# 870. Advantage Shuffle

# Greedy Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.06.22: yes
# notes: values can repeat, so map each nums2 value to a list of the
#        nums1 values assigned to it. Walk nums2 from largest down: spend
#        our biggest leftover if it beats it, else dump our smallest;
#        rebuild the answer in the original nums2 order.
class Solution:
    def advantageCount(self, nums1, nums2):
        assigned = {num2: [] for num2 in nums2}
        sorted_nums2 = sorted(nums2, reverse = True)
        sorted_nums1 = sorted(nums1, reverse = True)
        for j in range(len(sorted_nums2)):
            if sorted_nums1[0] > sorted_nums2[j]:
                assigned[sorted_nums2[j]].append(sorted_nums1.pop(0))
            else:
                assigned[sorted_nums2[j]].append(sorted_nums1.pop(-1))
            j += 1
        return [assigned[b].pop() for b in nums2]


# Tests:
for sol in (Solution(),):
    assert sol.advantageCount([2, 0, 4, 1, 2], [1, 3, 0, 0, 2]) == [2, 4, 1, 2, 0]
    assert sol.advantageCount([12, 24, 8, 32], [13, 25, 32, 11]) == [24, 32, 8, 12]
    assert sol.advantageCount([2, 7, 11, 15], [1, 10, 4, 11]) == [2, 11, 7, 15]
