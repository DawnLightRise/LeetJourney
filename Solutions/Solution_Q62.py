class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        df = [1] * n * m

        for i in range(1, m):
            for j in range(1, n):
                df[i * n + j] = df[(i - 1) * n + j] + df[i * n + j - 1]

        return df[m * n - 1]
