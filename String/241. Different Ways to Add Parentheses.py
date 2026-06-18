# 241. Different Ways to Add Parentheses

import functools
from typing import List


# Divide and conquer
# Time: O(n)
# Space: O(n)
# 2023.09.11: no
# notes: split at each operator into left and right results, then
#        combine every pair; ret.extend does the merge. Solution4 is my
#        own version which caches properly (the first one keeps clearing
#        m so it never really memoizes)
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        m = {}
        return self.dfs(expression, m)

    def dfs(self, input, m):
        if input in m:
            return m[input]
        if input.isdigit():
            m[input] = int(input)
            return [int(input)]
        ret = []
        for i, c in enumerate(input):
            if c in "+-*":
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i + 1:])
                ret.extend(eval(str(x) + c + str(y)) for x in l for y in r)
        m[input] = ret
        return ret


class Solution2:
    @functools.lru_cache(None)
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        res = []
        for i, x in enumerate(expression):
            if x in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                res += [eval(str(l) + x + str(r)) for l in left for r in right]

        return res


class Solution3:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if ('+' not in expression) and ('-' not in expression) and ('*' not in expression):
            return [int(expression)]

        res = []

        for i, v in enumerate(expression):
            if v == '+' or v == '-' or v == '*':
                left_res = self.diffWaysToCompute(expression[:i])
                right_res = self.diffWaysToCompute(expression[i + 1:])
                for left_i, left_v in enumerate(left_res):
                    for right_i, right_v in enumerate(right_res):
                        if v == '+':
                            res.append(left_v + right_v)
                        elif v == '-':
                            res.append(left_v - right_v)
                        else:
                            res.append(left_v * right_v)
        return res


class Solution4:
    def diffWaysToCompute(self, expression: str):
        self.m = {}
        return self.dfs(expression)

    def dfs(self, input):
        if input in self.m:
            return self.m[input]
        if input.isdigit():
            self.m[input] = [int(input)]
            return [int(input)]
        ret = []
        for i, c in enumerate(input):
            if c in "+-*":
                l = self.dfs(input[:i])
                r = self.dfs(input[i + 1:])
                ret.extend(eval(str(x) + c + str(y)) for x in l for y in r)
        self.m[input] = ret
        return ret


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sorted(sol.diffWaysToCompute("2-1-1")) == [0, 2]
    assert sorted(sol.diffWaysToCompute("2*3-4*5")) == [-34, -14, -10, -10, 10]
    assert sol.diffWaysToCompute("11") == [11]
