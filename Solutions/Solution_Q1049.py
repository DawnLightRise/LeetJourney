class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones_total = sum(stones)
        target = stones_total // 2
        
        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            for i in range(target - stone, -1, -1):
                if dp[i]:
                    dp[i + stone] = True

        for i in range(target, -1, -1):
            if dp[i]:
                return stones_total - i - i
