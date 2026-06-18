# 904. Fruit Into Baskets

# Sliding Window
# Time: O(n)
# Space: O(1)
# 2023.06.12: yes
# notes: slide a window keeping at most two fruit types; shrink
#        from the left when a third type appears
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        :type fruits: List[int]
        :rtype: int
        """
        basket = {}
        max_picked = 0
        left = 0
        for right in range(len(fruits)):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            max_picked = max(max_picked, right - left + 1)
        return max_picked


# Tests:
for sol in (Solution(),):
    assert sol.totalFruit([1, 2, 1]) == 3
    assert sol.totalFruit([0, 1, 2, 2]) == 3
    assert sol.totalFruit([1, 2, 3, 2, 2]) == 4
    assert sol.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
    assert sol.totalFruit([5]) == 1
