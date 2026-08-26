class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")":"(", 
                 "]":"[",
                 "}":"{"}

        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != pairs[c]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0