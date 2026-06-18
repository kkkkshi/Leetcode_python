# 17. Letter Combinations of a Phone Number

# Backtrack
# Time: O(4^N*N)
# Space: O(n)
# 2023.08.03: yes
# notes: map each digit to its letters and build strings by choosing
#        one letter per digit, backtracking when a string is complete
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def backtrack(index, cur):
            if len(cur) == len(digits):
                results.append("".join(cur))
                return
            possible_letters = letters[digits[index]]
            for i in possible_letters:
                cur.append(i)
                backtrack(index+1, cur)
                cur.pop()
        results = []
        backtrack(0, [])
        return results


# Tests:
for sol in (Solution(),):
    assert sol.letterCombinations("23") == [
        "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sol.letterCombinations("") == []
    assert sol.letterCombinations("2") == ["a", "b", "c"]
    assert sol.letterCombinations("9") == ["w", "x", "y", "z"]
