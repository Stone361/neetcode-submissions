class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for ch in tokens:
            if ch == '+':
                stk.append(stk.pop() + stk.pop())
            elif ch == '-':
                right = stk.pop()
                left = stk.pop()
                stk.append(left - right)
            elif ch == '*':
                stk.append(stk.pop() * stk.pop())
            elif ch == '/':
                right = stk.pop()
                left = stk.pop()
                stk.append(int(left / right))
            else:
                stk.append(int(ch))

        return stk[-1]