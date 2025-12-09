# Sorting (best method)
# Time: O(n+klogk)
# Space: O(k)
# 2023.09.12: yes
import heapq
from collections import Counter
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

# notes: 和上面方法一样，只不过我用的prev来记录前一个点，标答用的max_freq_allowed，因为是sorted所以我的方法不会
# 出现当前的可能性到更大的情况，因为只有deletion，如果还有insertion的话，他的方法应该会更好
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
# notes: 如果当前pop的和下一个一样，当前的就-1，然后塞进去，delete_count+1，以此往复
# 直到queue里没东西为止
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


# Decrement Each Duplicate Until it is Unique (不推荐)
# Time: O(n+k^2)
# Space: O(k)
# 2023.09.12: yes
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
test = Solution3()
test.minDeletions("abcabc")
test.minDeletions("ceabaacb")
test.minDeletions("aaabbbcc")




