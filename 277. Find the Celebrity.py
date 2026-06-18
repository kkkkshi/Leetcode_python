# 277. Find the Celebrity

# Logical Deduction Approach
# Time: O(n)
# Space: O(n)
# 2023.07.04: yes
# notes: pair people off; a candidate that knows someone or is not
#        known back is eliminated, leaving one to verify
class Solution:
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        q = []
        for i in range(n):
            q.append(i)
        while len(q) >= 2:
            cand = q.pop()
            other = q.pop()
            # cand knows someone -> not celeb; or other doesn't
            # know cand -> not celeb either
            if knows(cand, other) or not knows(other, cand):
                # cand can't be the celebrity, drop it, requeue other
                q.insert(0, other)
            else:
                q.insert(0, cand)
        cand = q.pop()

        for other in range(n):
            if other == cand:
                continue
            # everyone must know cand, and cand knows no one else
            if not knows(other, cand) or knows(cand, other):
                return -1
        return cand


# Logical Deduction Approach
# Time: O(n)
# Space: O(n)
# 2023.07.04: yes
# notes: keep a single candidate, replacing it whenever the test
#        shows it cannot be the celebrity, then verify
class Solution2:
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        cand = 0
        for other in range(1, n):
            # cand knows someone -> not celeb; or other doesn't
            # know cand -> not celeb either
            if knows(cand, other) or not knows(other, cand):
                cand = other
        for other in range(n):
            if other == cand:
                continue
            # everyone must know cand, and cand knows no one else
            if not knows(other, cand) or knows(cand, other):
                return -1
        return cand


# Logical Deduction with Caching
# Time: O(n)
# Space: O(n)
# 2023.07.04: no
# notes: cache knows so the api isn't called twice for a pair
from functools import lru_cache
class Solution3:
    @lru_cache(maxsize=None)
    def cachedKnows(self, a, b):
        return knows(a, b)
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        celebrity_candidate = 0
        for i in range(1, n):
            if self.cachedKnows(celebrity_candidate, i):
                celebrity_candidate = i
        if self.is_celebrity(celebrity_candidate):
            return celebrity_candidate
        return -1
    def is_celebrity(self, i):
        for j in range(self.n):
            if i == j: continue
            if self.cachedKnows(i, j) or not self.cachedKnows(j, i):
                return False
        return True


# Tests:
def make_knows(graph):
    def knows(a, b):
        return graph[a][b] == 1
    return knows


for cls in (Solution, Solution2, Solution3):
    # person 1 is the celebrity
    knows = make_knows([[1, 1, 0], [0, 1, 0], [1, 1, 1]])
    assert cls().findCelebrity(3) == 1
    # no celebrity
    knows = make_knows([[1, 0], [0, 1]])
    assert cls().findCelebrity(2) == -1
    # single person is the celebrity
    knows = make_knows([[1]])
    assert cls().findCelebrity(1) == 0
