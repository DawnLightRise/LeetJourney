class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            num0s = s.count('0')
            num1s = s.count('1')

            for i in range(m - num0s, -1, -1):
                for j in range(n - num1s, -1, -1):
                    i0 = i + num0s
                    j1 = j + num1s
                    dp[i0][j1] = max(dp[i0][j1], dp[i][j] + 1)

        return dp[m][n]
