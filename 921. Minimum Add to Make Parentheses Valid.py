# 921. Minimum Add to Make Parentheses Valid

# stack Approach
# Time: O(n)
# Space: O(n)
# 2023.09.29: yes
# notes: push '(' on the stack; on ')' pop a matching '(' or push the
#        ')' as unmatched; the leftover stack size is the answer
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        st = []
        for i in s:
            if i == "(":
                st.append(i)
            else:
                if st != [] and st[-1] == "(":
                    st.pop()
                else:
                    st.append(")")
        return len(st)


# Tests:
for sol in (Solution(),):
    assert sol.minAddToMakeValid("())") == 1
    assert sol.minAddToMakeValid("(((") == 3
    assert sol.minAddToMakeValid("()") == 0
    assert sol.minAddToMakeValid("()))((") == 4
