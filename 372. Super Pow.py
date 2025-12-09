# Recursion
# Time: O(n)
# Space: O(1)
# 2023.08.05: no
# notes: 核心还是recursion
from typing import List


class Solution:
    base = 1337  # 声明一个类变量 base

    # 声明一个实例方法 mypow
    def mypow(self, a, k):
        a %= self.base  # 对因子 a 求模
        res = 1
        for _ in range(k):
            res *= a  # 这里有乘法，是潜在的溢出点
            res %= self.base  # 对乘法结果求模
        return res

    # 声明一个实例方法 superPow
    def superPow(self, a, b):
        if not b:
            return 1
        last = b.pop()  # 取出 b 数组的最后一个元素
        part1 = self.mypow(a, last)  # 计算 a 的 last 次方
        part2 = self.mypow(self.superPow(a, b), 10)  # 递归计算 superPow(a, b[:len(b)-1]) 的 10 次方
        return (part1 * part2) % self.base  # 返回结果，每次都对结果求模

# Recursion
# Time: O(n)
# Space: O(1)
# 2023.08.05: no
# notes: 这个是根据奇偶性，b是奇数的话，a^b = a^(b-1) *a， b是偶数的话，a^b = a^(b//2)^2，效率是一样的，只是写的更简单了
# 9月3日update: 如果b = m* 10+d， a^b = a^d * a^10^m，这条是递归的关键，可以根据这条拆分b为一个个位数，
# 通过a^d，再计算a^m^10，利用性质1即可，其中a^m^10也是利用性质1
class Solution2:
    base = 1337

    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()  # 取出 b 数组的最后一个元素
        part1 = self.mypow(a, last)  # 计算 a 的 last 次方
        part2 = self.mypow(self.superPow(a, b), 10)  # 递归计算 superPow(a, b[:len(b)-1]) 的 10 次方
        return (part1 * part2) % self.base  # 返回结果，每次都对结果求模

    def mypow(self, a: int, k: int) -> int:
        if k == 0:
            return 1

        base = 1337
        a %= base

        if k % 2 == 1:
            # k 是奇数
            return (a * self.mypow(a, k - 1)) % base
        else:
            # k 是偶数
            sub = self.mypow(a, k // 2)
            return (sub * sub) % base
