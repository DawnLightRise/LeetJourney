class Solution:
    def __init__(self):
        self.results = []
        self.path = []
        self.n = 1

    def restoreIPAddresses_helper_dfs(self, s: str, start: int) -> None:
        if len(self.path) == 4:
            if start == self.n:
                self.results.append(".".join(self.path))
                
            return

        for i in range(start, min(start + 3, self.n)):
            if s[start] == '0' and i > start:
                break

            segment = s[start: i + 1]
            if int(segment) > 255:
                break
            self.path.append(segment)
            self.restoreIPAddresses_helper_dfs(s, i + 1)
            self.path.pop()


    def restoreIpAddresses(self, s: str) -> List[str]:
        self.results = []
        self.path = []
        self.n = len(s)

        self.restoreIPAddresses_helper_dfs(s, 0)

        return self.results
