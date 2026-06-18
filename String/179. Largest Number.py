# 179. Largest Number

# Sorting via Custom Comparator Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.07.05: yes
# notes: very concise; sort numbers as strings by comparing a+b vs b+a
class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


# Tests:
for sol in (Solution(),):
    assert sol.largestNumber([10, 2]) == '210'
    assert sol.largestNumber([3, 30, 34, 5, 9]) == '9534330'
    assert sol.largestNumber([0, 0]) == '0'
    assert sol.largestNumber([1]) == '1'
