class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        operators = set(['+', '-', '*', '/'])
        operator = '+'
        stack = []
        last_i = len(s) - 1
        num = 0

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            if char in operators or i == last_i:
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
