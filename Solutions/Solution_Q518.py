class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(0, amount - coin + 1):
                dp[coin + i] += dp[i]

        return dp[amount]
