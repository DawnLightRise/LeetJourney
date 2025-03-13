class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)

        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = 0 # Idle
        dp[0][1] = -prices[0] # Buy / Hold
        dp[0][2] = 0 # Sell

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = dp[i-1][1] + prices[i]

        return max(dp[n-1][0], dp[n-1][2])
