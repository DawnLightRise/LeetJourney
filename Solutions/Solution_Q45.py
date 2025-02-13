class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        boundary = 0
        maxReach = 0

        for i in range(n):
            maxReach = max(maxReach, i + nums[i])

            if boundary >= n - 1:
                return count

            if i == boundary:
                count += 1
                boundary = maxReach

        return -1
