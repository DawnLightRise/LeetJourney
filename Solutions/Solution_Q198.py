class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        prev, cur = 0, nums[0]

        for num in nums[1:]:
            prev, cur = cur, max(cur, prev + num)

        return cur
