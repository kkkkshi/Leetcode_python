# BruteForce (TLE)
# Time: O(n^2)
# Space: O(n)
# 2023.09.13: no
from typing import List
# notes: 如果当前比前面大，就+1， 比前面小就-1，有更改就changed = True，直到没有changed，就结束了
class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n
        has_changed = True

        while has_changed:
            has_changed = False
            for i in range(n):
                if (
                    i < n - 1
                    and ratings[i] > ratings[i + 1]
                    and candies[i] <= candies[i + 1]
                ):
                    candies[i] = candies[i + 1] + 1
                    has_changed = True
                if (
                    i > 0
                    and ratings[i] > ratings[i - 1]
                    and candies[i] <= candies[i - 1]
                ):
                    candies[i] = candies[i - 1] + 1
                    has_changed = True
        return sum(candies)


# Using two arrays
# Time: O(n)
# Space: O(n)
# 2023.09.13: no
# notes: 列两个array，一个从左到右，一个从右到左，遇到更大的就+1，遍历完两个array之后取max即可
class Solution2:
    def candy(self, ratings):
        n = len(ratings)
        sum = 0
        left2right = [1] * n
        right2left = [1] * n

        # Scan from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1

        # Scan from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right2left[i] = right2left[i + 1] + 1

        # Calculate the total number of candies
        for i in range(n):
            sum += max(left2right[i], right2left[i])

        return sum


# Using one arrays
# Time: O(n)
# Space: O(n)
# 2023.09.13: no
# notes: 和上面差不多，只是用一个来存罢了，记录一下最右边的点就可以优化一点空间，有用，但不多
class Solution3:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n
        # Scan from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        sum = candies[n - 1]
        # Scan from right to left and update candies
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
            sum += candies[i]
        return sum


# Single Pass Approach with Constant Space
# Time: O(n)
# Space: O(1)
# 2023.09.13: no
# notes: 没看懂，但是solution5写了O(1)的方法，也有一部分没懂，之后update
class Solution4:
    def count(self, n):
        return (n * (n + 1)) // 2

    def candy(self, ratings):
        if len(ratings) <= 1:
            return len(ratings)

        candies = 0
        up = 0
        down = 0
        old_slope = 0

        for i in range(1, len(ratings)):
            new_slope = (
                1
                if ratings[i] > ratings[i - 1]
                else (-1 if ratings[i] < ratings[i - 1] else 0)
            )

            if (old_slope > 0 and new_slope == 0) or (old_slope < 0 and new_slope >= 0):
                candies += self.count(up) + self.count(down) + max(up, down)
                up = 0
                down = 0

            if new_slope > 0:
                up += 1
            elif new_slope < 0:
                down += 1
            else:
                candies += 1

            old_slope = new_slope

        candies += self.count(up) + self.count(down) + max(up, down) + 1
        return candies


# Single Pass Approach with Constant Space
# Time: O(n)
# Space: O(1)
# 2023.09.13: no
# notes: 根据每个点的状态和前一个的状态，考虑当前应该加多少点数
# 如果是单纯increase，直接加这是第几个增加的点即可，但是如果increase的时候，之前有down的情况，说明这是个谷底，这时候
# 就可以reset, down, up = 0, 1让这个点作为起始点，因为down下来的时候，3,2,1最后一定是1，否则就拿多candy了
# 所以新的起始点，是1+1 = 2
# 如果是平的情况，也是reset, down, up = 0, 1但是这次是平，所以up不需要+2，只需要+1即可
# 如果是down的情况，比如4,3,2这样下来，完全可以给他赋予1,2,3个candy，是可以交换的，所以每次只要计算有几个down即可
# 如果down >= up 唯一的情况就是平之后直接down，否则其余情况会被increase覆盖，直接down的话，就在平的基础上
# 1+1，因为平的时候是1，现在比平要低，起始点就是2了
class Solution5:
    def candy(self, ratings: List[int]) -> int:
        ans = down = up = 0
        for i in range(len(ratings)):
            if not i or ratings[i - 1] < ratings[i]:
                if down:
                    down, up = 0, 1
                up += 1
                ans += up
            elif ratings[i - 1] == ratings[i]:
                down, up = 0, 1
                ans += 1
            else:
                down += 1
                ans += down if down < up else down + 1
        return ans


# Tests:
test = Solution5()
#           1  2  3  4  5  1  2  3 1+1 3  1  2  3  1  2  3  1  2  1  1  2  1
test.candy([1, 2, 3, 4, 5, 3, 2, 1, 2, 6, 5, 4, 3, 3, 2, 1, 1, 3, 3, 3, 4, 2])
test.candy([1, 3, 2, 2, 1])  # 7
test.candy([1, 0, 2])
