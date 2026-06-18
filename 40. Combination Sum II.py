# 40. Combination Sum II

# Backtracking
# Time: O(2^n)
# Space: O(n)
# 2023.08.03: yes
# notes: build a (num, count) list from a Counter; during backtracking
#        decrement a count when used so each element is not reused.
from collections import Counter


class Solution:
    def combinationSum2(self, candidates, target):

        def backtrack(comb, remain, curr, counter, results):
            if remain == 0:
                # make a deep copy of the current combination
                #   rather than keeping the reference.
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for next_curr in range(curr, len(counter)):
                candidate, freq = counter[next_curr]

                if freq <= 0:
                    continue

                # add a new element to the current combination
                comb.append(candidate)
                counter[next_curr] = (candidate, freq-1)

                # continue the exploration with the updated combination
                backtrack(comb, remain - candidate, next_curr, counter, results)

                # backtrack the changes, so that we can try another candidate
                counter[next_curr] = (candidate, freq)
                comb.pop()

        results = []  # container to hold the final combinations
        counter = Counter(candidates)
        # convert the counter table to a list of (num, count) tuples
        counter = [(c, counter[c]) for c in counter]

        backtrack(comb = [], remain = target, curr = 0,
                  counter = counter, results = results)

        return results


# Backtracking
# Time: O(2^n)
# Space: O(n)
# 2023.08.03: yes
# notes: sort to prune (a too-large pick ends the branch); skip a
#        candidate equal to its previous sibling to avoid duplicates.
class Solution2:
    def combinationSum2(self, candidates, target):

        def backtrack(comb, remain, curr, results):

            if remain == 0:
                # make a deep copy of the resulted combination
                results.append(list(comb))
                return

            for next_curr in range(curr, len(candidates)):

                if next_curr > curr and candidates[next_curr] == candidates[next_curr - 1]:
                    continue

                pick = candidates[next_curr]
                # optimization: skip the rest of elements starting from 'curr' index
                if remain - pick < 0:
                    break

                comb.append(pick)
                backtrack(comb, remain - pick, next_curr + 1, results)
                comb.pop()

        candidates.sort()

        comb, results = [], []
        backtrack(comb, target, 0, results)

        return results


# Tests:
def norm(combos):
    return sorted(sorted(c) for c in combos)


for sol in (Solution(), Solution2()):
    assert norm(sol.combinationSum2([2, 5, 2, 1, 2], 5)) == [[1, 2, 2], [5]]
    assert norm(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)) == \
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    assert sol.combinationSum2([2, 2, 2], 5) == []
