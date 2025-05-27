class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in hashmap:
                if not stack:
                    return False
                else:
                    if hashmap[char] != stack.pop():
                        return False
            else:
                stack.append(char)

        return not stack