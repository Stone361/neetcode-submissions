class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operators = {'+', '-', '*', '/'}

        for t in tokens:
            if t not in operators:
                stk.append(int(t))
                continue

            right = stk.pop()
            left = stk.pop()

            if t == '+':
                res = left + right
            elif t == '-':
                res = left - right
            elif t == '*':
                res = left * right
            elif t == '/':
                res = int(left / right)
            stk.append(res)
        
        return stk.pop()
            