class Solution:
    def rob_helper(self, nums: List[int]) -> int:
        prev, cur = 0, nums[0]
        for num in nums[1:]:
            prev, cur = cur, max(cur, prev + num)
        return cur

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        rob_out_0 = self.rob_helper(nums[1:])
        rob_out_n = self.rob_helper(nums[:-1])
        
        return max(rob_out_0, rob_out_n)
