class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        m = len(s)
        i = 0

        for char in t:
            if char == s[i]:
                i += 1
            if i == m:
                return True

        return False
