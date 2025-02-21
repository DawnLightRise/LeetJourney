class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove = []
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    remove.append(i)

        while stack:
            remove.append(stack.pop())

        remove_set = set(remove)
        
        res = []
        for i, char in enumerate(s):
            if i not in remove_set:
                res.append(char)

        return "".join(res)
