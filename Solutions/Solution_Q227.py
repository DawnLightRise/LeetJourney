class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        operators = set(['+', '-', '*', '/'])
        last = len(s) - 1

        stack = []
        num = 0
        operator = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            if char in operators or i == last:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))

                operator = char
                num = 0

        return sum(stack)
