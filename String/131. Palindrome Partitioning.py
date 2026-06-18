# 131. Palindrome Partitioning

# Backtracking
# Time: O(n*2^n)
# Space: O(n)
# 2023.10.30: no
# notes: try every cut; if the prefix is a palindrome, recurse on
#        the rest and backtrack
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
# notes: see Solution3 for the proper dp version
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


# Backtracking with Dynamic Programming
# Time: O(n*2^n)
# Space: O(n^2)
# 2023.10.30: no
# notes: fill each cell from start+1/end-1 and start==end, so no
#        separate palindrome check is needed
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
for sol in (Solution(), Solution2(), Solution3()):
    assert sol.partition("aab") == [["a", "a", "b"], ["aa", "b"]]
    assert sol.partition("a") == [["a"]]
    assert sol.partition("ab") == [["a", "b"]]
    assert sol.partition("aba") == [["a", "b", "a"], ["aba"]]
