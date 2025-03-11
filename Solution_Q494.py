class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_total = sum(nums)
        if nums_total < abs(target) or (nums_total + target) % 2 != 0:
            return 0
        
        n = (nums_total + target) // 2
        dp = [0] * (n + 1)
        dp[0] = 1

        for num in nums:
            for i in range(n - num, -1, -1):
                dp[num + i] += dp[i]

        return dp[n]
