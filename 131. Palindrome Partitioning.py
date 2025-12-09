# Backtracking
# Time: O(n*2^n)
# Space: O(n)
# 2023.10.30: no

from typing import List
class Solution:
    def partition(self, s):
        result = []
        self.dfs(0, [], result, s)
        return result

    def dfs(self, start, current_list, result, s):
        if start >= len(s):
            result.append(current_list[:])
            return
        for end in range(start, len(s)):
            if self.palindrome(s[start : end + 1]):
                current_list.append(s[start : end + 1])
                self.dfs(end + 1, current_list, result, s)
                current_list.pop()

    def palindrome(self, s):
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                return False
        return True


# Backtracking with Dynamic Programming
# Time: O(n*2^n)
# Space: O(n^2)
# 2023.10.30: no
# notes: 看solution3，才是dp正确版本
class Solution2:
    def partition(self, s):
        result = []
        self.dp = [[-1]*(len(s)+1) for _ in range(len(s)+1)]
        self.dfs(0, [], result, s)
        return result

    def dfs(self, start, current_list, result, s):
        if start >= len(s):
            result.append(current_list[:])
            return
        for end in range(start, len(s)):
            if self.dp[start][end] == -1:
                self.palindrome(s, start, end)
                flag = self.dp[start][end]
            else:
                flag = self.dp[start][end]
            if flag:
                current_list.append(s[start : end + 1])
                self.dfs(end + 1, current_list, result, s)
                current_list.pop()

    def palindrome(self, s, start, end):
        start_set, end_set = start, end
        while start < end:
            if s[start] != s[end]:
                self.dp[start_set][end_set] = False
                return
            start += 1
            end -= 1
        self.dp[start_set][end_set] = True

# notes: 根据前一个start+1, end-1和start == end去解析最新的格子，不用计算palindrome
class Solution3:
    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        dp = [[False] * length for _ in range(length)]
        result = []
        self.dfs(result, s, 0, [], dp)
        return result

    def dfs(self, result, s, start, currentList, dp):
        if start >= len(s):
            result.append(currentList[:])
        for end in range(start, len(s)):
            if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                dp[start][end] = True
                currentList.append(s[start:end + 1])
                self.dfs(result, s, end + 1, currentList, dp)
                currentList.pop()


# Tests:
test = Solution2()
test.partition("abbab")
test.partition("aab")


