# 772. Basic Calculator III

# Solve Isolated Expressions With Recursion
# Time: O(n)
# Space: O(1)
# 2023.09.29: yes
# notes: keep an index pointer to track the current position and a
#        stack for running values; recurse into each parenthesis
class Solution:
    def calculate(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        def evaluate(x, y, operator):
            if operator == "+":
                return x
            if operator == "-":
                return -x
            if operator == "*":
                return x * y
            return int(x / y)

        def solve(i):
            stack = []
            curr = 0
            previous_operator = "+"

            while i[0] < len(s):
                c = s[i[0]]
                if c == "(":
                    i[0] += 1
                    curr = solve(i)
                elif c.isdigit():
                    curr = curr * 10 + int(c)
                else:
                    if previous_operator in "*/":
                        stack.append(evaluate(stack.pop(), curr, previous_operator))
                    else:
                        stack.append(evaluate(curr, 0, previous_operator))

                    if c == ")":
                        break

                    curr = 0
                    previous_operator = c

                i[0] += 1

            return sum(stack)

        s += "@"
        return solve([0])


# Tests:
for sol in (Solution(),):
    assert sol.calculate("2*(5+5*2)/3+(6/2+8)") == 21
    assert sol.calculate("1+1") == 2
    assert sol.calculate("6-4/2") == 4
    assert sol.calculate("2*3+(4-2)") == 8
