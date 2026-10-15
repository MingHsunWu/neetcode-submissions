class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ("+", "-", "*", "/"):
                right = stack.pop()
                left = stack.pop()
                if t == "+":
                    res = left + right
                if t == "-":
                    res = left - right
                if t == "*":
                    res = left * right
                if t == "/":
                    res = int(left / right)
                stack.append(res)

            else:
                stack.append(int(t))
        return stack[-1]