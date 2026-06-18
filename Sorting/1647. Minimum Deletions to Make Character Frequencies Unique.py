# 1647. Minimum Deletions to Make Character Frequencies Unique

import heapq
from collections import Counter


# Sorting (best method)
# Time: O(n+klogk)
# Space: O(k)
# 2023.09.12: yes
# notes: sort counts descending; each count must be below the previous
#        kept one, so delete down to it and tally the deletions
class Solution:
    def minDeletions(self, s: str) -> int:
        results = 0
        char_count = Counter(s)
        counts = sorted(char_count.values(), reverse=True)
        prev = float("inf")
        for i in counts:
            if i <= prev:
                prev = i
                prev -= 1
            else:
                results += (i - prev)
                if prev > 0:
                    prev -= 1
        return results


# Sorting (max frequency allowed)
# Time: O(n+klogk)
# Space: O(k)
# 2023.09.12: yes
# notes: same idea as above but tracked with max_freq_allowed instead
#        of prev; since it is sorted my version never overshoots, but
#        with insertion allowed this version would be better
class Solution2:
    def minDeletions(self, s: str) -> int:

        # Store the frequency of each character
        frequency = [0] * 26
        for char in s:
            frequency[ord(char) - ord('a')] += 1
        frequency.sort(reverse=True)

        delete_count = 0
        # Maximum frequency the current character can have
        max_freq_allowed = len(s)

        # Iterate over the frequencies in descending order
        for freq in frequency:
            # Delete characters to make the frequency equal the maximum frequency allowed
            if freq > max_freq_allowed:
                delete_count += freq - max_freq_allowed
                freq = max_freq_allowed

            # Update the maximum allowed frequency
            max_freq_allowed = max(0, freq - 1)

        return delete_count


# Priority Queue
# Time: O(n+k^2logk)
# Space: O(k)
# 2023.09.12: no
# notes: if the popped count equals the next one, decrement it, push it
#        back and add one deletion; repeat until the queue is empty
class Solution3:
    def minDeletions(self, s: str) -> int:

        # Store the frequency of each character
        frequency = [0] * 26
        for char in s:
            frequency[ord(char) - ord('a')] += 1

        # Add all non-zero frequencies to max priority queue
        # Create a max priority queue by flipping the sign of each element
        pq = [-freq for freq in frequency if freq != 0]
        heapq.heapify(pq)

        delete_count = 0
        while len(pq) > 1:
            # Flip the sign back to positive when removing from the max priority queue
            top_element = -heapq.heappop(pq)

            # If the top two elements in the priority queue are the same
            if top_element == -pq[0]:
                # Decrement the popped value and push it back into the queue
                if top_element - 1 > 0:
                    top_element -= 1
                    heapq.heappush(pq, -top_element)

                delete_count += 1

        return delete_count


# Decrement Each Duplicate Until it is Unique (not recommended)
# Time: O(n+k^2)
# Space: O(k)
# 2023.09.12: yes
# notes: for each count, keep decrementing while it is already in the
#        seen set, then record the count we settled on
class Solution4:
    def minDeletions(self, s: str) -> int:

        # Store the frequency of each character
        frequency = [0] * 26
        for char in s:
            frequency[ord(char) - ord('a')] += 1

        delete_count = 0
        # Use a set to store the frequencies we have already seen
        seen_frequencies = set()
        for i in range(26):
            # Keep decrementing the frequency until it is unique
            while frequency[i] and frequency[i] in seen_frequencies:
                frequency[i] -= 1
                delete_count += 1

            # Add the newly occupied frequency to the set
            seen_frequencies.add(frequency[i])

        return delete_count


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.minDeletions("abcabc") == 3
    assert sol.minDeletions("ceabaacb") == 2
    assert sol.minDeletions("aaabbbcc") == 2
    assert sol.minDeletions("aab") == 0
    assert sol.minDeletions("a") == 0
