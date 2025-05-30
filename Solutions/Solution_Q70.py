class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        cur, prev = 2, 1

        for i in range(2, n):
            cur, prev = cur + prev, cur

        return cur
