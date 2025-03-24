class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [-inf] * (n + 1)

        for i in range(n):
            dp[i+1] = max(dp[i] + nums[i], nums[i])
        
        return max(dp[1:])
