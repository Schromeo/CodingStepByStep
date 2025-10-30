'''
Calculator
'''
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        num, stack, op = 0, [], '+'
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if not ch.isdigit() or i == len(s)- 1:
                if op == '+': stack.append(num)
                elif op == '-': stack.append(-num)
                elif op == '*': stack[-1] *= num
                elif op == '/': stack[-1] = int(stack[-1] / num)
                op = ch
                num = 0
        return sum(stack)

test = Solution()
print(test.calculate("1+2*9/3"))

class SolutionForPlusMinusParenthese:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num = 0
        sign = 1  # 当前符号（1或-1）

        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch in ['+', '-']:
                res += sign * num
                sign = 1 if ch == '+' else -1
                num = 0
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ')':
                res += sign * num
                res *= stack.pop()  # sign
                res += stack.pop()  # previous res
                num = 0
        return res + sign * num
 