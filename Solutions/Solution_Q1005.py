class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        if k == 0:
            return sum(nums)

        if not nums:
            return 0

        n = len(nums)
        nums.sort()

        for i in range(n):
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
                if k == 0:
                    break
            else:
                break

        total_sum = sum(nums)
        min_value = min(nums)
        
        if k % 2 == 1:
            total_sum -= 2 * min_value

        return total_sum
