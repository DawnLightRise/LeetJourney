class Solution:
    def __init__(self):
        pass

    def isPalindrome(self, s: str, left: int, right: int):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if self.isPalindrome(s, left + 1, right):
                    return True
                elif self.isPalindrome(s, left, right - 1):
                    return True
                else:
                    return False

        return True