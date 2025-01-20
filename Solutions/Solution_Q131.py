class Solution:
    def __init__(self):
        self.results = []
        self.path = []
        self.n = 1

    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
    
    def partition_helper_dfs(self, s: str, start: int) -> None:
        if start == self.n:
            self.results.append(self.path[:])
            return 

        for i in range(start, self.n):
            if self.is_palindrome(s, start, i):
                self.path.append(s[start: i + 1])
                self.partition_helper_dfs(s, i + 1)
                self.path.pop()


    def partition(self, s: str) -> List[List[str]]:
        self.results = []
        self.path = []
        self.n = len(s)

        self.partition_helper_dfs(s, 0)

        return self.results
