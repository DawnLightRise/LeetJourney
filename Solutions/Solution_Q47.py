class Solution:
    def __init__(self):
        self.results = []
        self.path = []

    def permuteUnique_helper_dfs(self, nums: List[int]) -> None:
        if not nums:
            self.results.append(self.path[:])
            return

        used_current_level = []
        for i in range(len(nums)):
            if nums[i] not in used_current_level:
                self.path.append(nums[i])
                used_current_level.append(nums[i])
                self.permuteUnique_helper_dfs(nums[:i] + nums[i+1:])
                self.path.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.path = []

        self.permuteUnique_helper_dfs(nums)

        return self.results
