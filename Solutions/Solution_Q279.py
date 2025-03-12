import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        m = int(math.sqrt(n))

        for i in range(2, n + 1):
            for j in range(1, m + 1):
                j2 = j * j
                if j2 > i:
                    break
                dp[i] = min(dp[i], dp[i - j2] + 1)

        return dp[n]
