class Solution:
    def __init__(self):
        self.results = []
        self.path = []
        self.n = 1

    def subsetsWithDup_helper_dfs(self, nums: List[int], start: int) -> None:
        self.results.append(self.path[:])

        for i in range(start, self.n):
            if i > start and nums[i] == nums[i-1]:
                continue

            self.path.append(nums[i])
            self.subsetsWithDup_helper_dfs(nums, i + 1)
            self.path.pop()

        return self.results

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.path = []
        self.n = len(nums)

        nums.sort()
        self.subsetsWithDup_helper_dfs(nums, 0)

        return self.results
