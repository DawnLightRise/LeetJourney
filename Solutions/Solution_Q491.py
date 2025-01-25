class Solution:
    def __init__(self):
        self.results = []
        self.path = []
        self.n = 1

    def findSubSequences_helper_dfs(self, nums: List[int], start: int) -> None:
        if len(self.path) > 1:
            self.results.append(self.path[:])

        used_for_current_level = []
        for i in range(start, self.n):
            if ((not self.path) or (nums[i] >= self.path[-1])) and (nums[i] not in used_for_current_level):
                self.path.append(nums[i])
                used_for_current_level.append(nums[i])
                self.findSubSequences_helper_dfs(nums, i + 1)
                self.path.pop()

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.path = []
        self.n = len(nums)

        self.findSubSequences_helper_dfs(nums, 0)

        return self.results
