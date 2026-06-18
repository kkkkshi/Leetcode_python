# 20. Valid Parentheses

# stack Approach
# Time: O(n)
# Space: O(n)
# 2023.07.17: yes
# notes: push openers; on a closer, pop and check it matches the
#        expected opener; valid only if the stack ends empty
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack


# Tests:
for sol in (Solution(),):
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("()") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("([)]") is False
    assert sol.isValid("(") is False
