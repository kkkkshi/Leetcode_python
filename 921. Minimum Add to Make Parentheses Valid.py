# stack Approach
# Time: O(n)
# Space: O(n)
# 2023.09.29: yes

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
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




test = Solution()
test.minAddToMakeValid("())") # 1
test.minAddToMakeValid("(((") # 3