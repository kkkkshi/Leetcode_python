# 969. Pancake Sorting

# Recursion Approach
# Time: O(n^2)
# Space: O(n)
# 2023.08.03: no
# notes: do we really need recursion here? same idea either way: find
#        the largest, flip it to the top, then flip it to the bottom
class Solution:
    def pancakeSort(self, cakes):
        """
        :type cakes: List[int]
        :rtype: List[int]
        """
        # record the sequence of flips
        self.res = []
        self.sort(cakes, len(cakes))
        return self.res

    def sort(self, cakes, n):
        # base case
        if n == 1:
            return
        # find the index of the largest pancake
        max_cake = 0
        max_cake_index = 0
        for i in range(n):
            if cakes[i] > max_cake:
                max_cake_index = i
                max_cake = cakes[i]
        # first flip: bring the largest pancake to the top
        self.reverse(cakes, 0, max_cake_index)
        self.res.append(max_cake_index + 1)
        # second flip: bring the largest pancake to the bottom
        self.reverse(cakes, 0, n - 1)
        self.res.append(n)

        # recurse
        self.sort(cakes, n - 1)

    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1


# Recursion Approach
# Time: O(n^2)
# Space: O(n)
# 2023.08.03: no
# notes: the problem is vague because it doesn't say the array is a
#        permutation of 1..k; a random array won't work, you'd first
#        find the max, but each value still takes at most two flips
class Solution2:
    def pancakeSort(self, A):
        """ sort like bubble-sort
            sink the largest number to the bottom at each round
        """
        def flip(sublist, k):
            i = 0
            while i < k / 2:
                sublist[i], sublist[k-i-1] = sublist[k-i-1], sublist[i]
                i += 1

        ans = []
        value_to_sort = len(A)
        while value_to_sort > 0:
            # locate the position for the value to sort in this round
            index = A.index(value_to_sort)

            # sink the value_to_sort to the bottom,
            #   with at most two steps of pancake flipping.
            if index != value_to_sort - 1:
                # flip the value to the head if necessary
                if index != 0:
                    ans.append(index+1)
                    flip(A, index+1)
                # now that the value is at the head, flip it to the bottom
                ans.append(value_to_sort)
                flip(A, value_to_sort)

            # move on to the next round
            value_to_sort -= 1

        return ans


def apply_flips(arr, flips):
    a = arr[:]
    for k in flips:
        a[:k] = a[:k][::-1]
    return a


# Tests:
# inputs are permutations of 1..n (Solution2 requires this)
for sol in (Solution(), Solution2()):
    for arr in ([3, 2, 4, 1], [1, 2, 3], [4, 3, 2, 1], [1]):
        flips = sol.pancakeSort(arr[:])
        assert apply_flips(arr, flips) == sorted(arr)
