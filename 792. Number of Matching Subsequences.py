# 792. Number of Matching Subsequences

from bisect import bisect_right
from collections import defaultdict
from typing import List


# Greedy Match with Character Indices Hashmap
# Time: O(S.length+∑iwords[i].length)
# Space: O(word length)
# 2023.10.01: no
# notes: store each letter's positions in s; for every word, binary
#        search the next position strictly after the last match
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        letter_indices_table = defaultdict(list)
        for index, letter in enumerate(s):
            letter_indices_table[letter].append(index)
        result = 0
        for word in words:
            curr_match_index = -1
            matched = 0
            for letter in word:
                if letter not in letter_indices_table:
                    break
                indices_list = letter_indices_table[letter]
                match_index = bisect_right(indices_list, curr_match_index)
                if match_index != len(indices_list):
                    curr_match_index = indices_list[match_index]
                    matched += 1
                else:
                    break
            if matched == len(word):
                result += 1
        return result


# Next Letter Pointers
# Time: O(S.length+∑iwords[i].length)
# Space: O(word length)
# 2023.10.01: no
# notes: bucket each word by its first letter as an iterator; scan s and
#        advance matched iterators, counting one when an iterator empties
class Solution2:
    def numMatchingSubseq(self, S, words):
        ans = 0
        heads = [[] for _ in range(26)]
        for word in words:
            it = iter(word)
            heads[ord(next(it)) - ord('a')].append(it)

        for letter in S:
            letter_index = ord(letter) - ord('a')
            old_bucket = heads[letter_index]
            heads[letter_index] = []

            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1
        return ans


# Tests:
for sol in (Solution(), Solution2()):
    assert sol.numMatchingSubseq("abcde", ["a","bb","acd","ace"]) == 3
    assert sol.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]) == 2
    assert sol.numMatchingSubseq("abc", []) == 0
