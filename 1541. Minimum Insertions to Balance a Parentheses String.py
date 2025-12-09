# Greedy
# Time: O(n)
# Space: O(1)
# 2023.09.29: no
# notes: 常规遍历一遍，但是要注意的细节是如果右括号是1的情况怎么办，需要特殊处理
# 遇到左括号，右括号需求+2，如果需求%2=1的话，说明前一步只有一个右括号就结束了，左括号需求需要+1， 右括号需求因为刚才是1，所以-1
# 遇到右括号，右括号需求-1，但是如果右括号需求是负数，说明，没有左括号，左括号需求+1， 现在还需要1个右括号补足刚才的左括号
class Solution:
    def minInsertions(self, s: str) -> int:
        res, need = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                need += 2
                if need % 2 == 1:
                    res += 1 # 因为右括号需要匹配两个，只有一个，需要补一个左括号，不然不会是奇数
                    need -= 1
            elif s[i] == ')':
                need -= 1
                if need == -1:
                    res += 1
                    need = 1
        return res + need


test = Solution()
test.minInsertions("()(")
test.minInsertions("(()))") # 1
test.minInsertions("())") # 0
test.minInsertions("))())(") # 3