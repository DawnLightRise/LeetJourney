class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        res = nums[0]
        tmp = max(0, nums[0])

        for i in range(1, n):
            tmp += nums[i]   
            res = max(res, tmp)
            if tmp < 0:
                tmp = 0

        return res
