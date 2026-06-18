# 780. Reaching Points

# Exhaustive Search [Time Limit Exceeded]
# Time: O(2^n)
# Space: O(tx*ty)
# 2023.07.17: yes
# notes: from (x, y) branch to (x+y, y) and (x, x+y); recurse until
#        the target is hit or the coordinates overshoot it
class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        if sx > tx or sy > ty: return False
        if sx == tx and sy == ty: return True
        return self.reachingPoints(sx+sy, sy, tx, ty) or \
               self.reachingPoints(sx, sx+sy, tx, ty)


# Dynamic Programming [Time Limit Exceeded]
# Time: O(tx*ty)
# Space: O(tx*ty)
# 2023.07.17: yes
# notes: memoize visited points while exploring forward, then check
#        whether the target was reached
class Solution2:
    def reachingPoints(self, sx, sy, tx, ty):
        seen = set()
        def search(x, y):
            if (x, y) in seen: return
            if x > tx or y > ty: return
            seen.add((x, y))
            search(x+y, y)
            search(x, x+y)

        search(sx, sy)
        return (tx, ty) in seen


# Work Backwards [Time Limit Exceeded]
# Time: O(max(tx, ty))
# Space: O(1)
# 2023.07.17: yes
# notes: Every parent point (x, y) has two children, (x, x+y) and (x+y, y).
# However, every point (x, y) only has one parent candidate (x-y, y) if x >= y, else (x, y-x).
# This is because we never have points with negative coordinates.
# notes: this is the key idea: coordinates can't be negative, so each
#        parent has only one possible child
class Solution3:
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if sx == tx and sy == ty: return True
            if tx > ty:
                tx -= ty
            else:
                ty -= tx
        return False


# Work Backwards (Modulo Variant)
# Time: O(log(max(tx, ty)))
# Space: O(1)
# 2023.07.17: yes
# notes: same as above, but once a coordinate drops below the start
#        only one path remains, so use (tx-sx)%ty to check it
class Solution4:
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy


# Tests:
for sol in (Solution(), Solution2(), Solution3(), Solution4()):
    assert sol.reachingPoints(1, 1, 3, 5) is True
    assert sol.reachingPoints(1, 1, 2, 2) is False
    assert sol.reachingPoints(1, 1, 1, 1) is True
    assert sol.reachingPoints(3, 3, 12, 9) is True
