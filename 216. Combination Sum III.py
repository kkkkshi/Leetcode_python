# 216. Combination Sum III

# Backtracking
# Time: O((9！k)/(9-k)!)
# Space: O(k)
# 2023.08.03: yes
# notes: pick increasing digits 1..9, recurse while tracking the
#        remaining sum and count
class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        cur = []
        start = 1
        self.backtracking(k, n, cur, results, start)
        return results

    def backtracking(self, k, n, cur, results, start):
        if n == 0 and k == 0:
            results.append(cur[:])
        elif n < 0:
            return
        elif k == 0:
            return
        for i in range(start,10):
            if cur == [] or i > cur[-1]:
                cur.append(i)
                self.backtracking(k-1, n-i, cur, results, start+1)
                cur.pop()


# Backtracking
# Time: O((9！k)/(9-k)!)
# Space: O(k)
# 2023.08.03: yes
# notes: simpler version, start each branch from the next index
#        instead of scanning from the beginning
class Solution2:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(remain-i-1, comb, i+1)
                # backtrack the current choice
                comb.pop()

        backtrack(n, [], 0)

        return results


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.combinationSum3(3, 7) == [[1, 2, 4]]
    assert sol.combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    assert sol.combinationSum3(4, 1) == []
    assert sol.combinationSum3(2, 18) == []
