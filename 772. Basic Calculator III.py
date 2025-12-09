# Solve Isolated Expressions With Recursion
# Time: O(n)
# Space: O(1)
# 2023.09.29: yes
# notes: 这道题与之前的不同就是需要有一个global variable去记录现在的位数，并且需要用stack记录目前的值，需要用recursion去调用括号内的内容

class Solution:
    def calculate(self, s: str) -> int:
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



test = Solution()
test.calculate("2*(5+5*2)/3+(6/2+8)")