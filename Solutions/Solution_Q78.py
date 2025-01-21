class Solution:
    def __init__(self):
        self.results = []
        self.path = []
        self.n = 1

    def subsets_helper_dfs(self, nums: List[int], start: int) -> None:
        self.results.append(self.path[:])

        for i in range(start, self.n):
            self.path.append(nums[i])
            self.subsets_helper_dfs(nums, i + 1)
            self.path.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.path = []
        self.n = len(nums)

        self.subsets_helper_dfs(nums, 0)

        return self.results
