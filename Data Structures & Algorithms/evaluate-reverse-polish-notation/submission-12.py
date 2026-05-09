class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token not in ["+","-","*","/"]:
                stack.append(int(token))
            else:
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()

                    if token == "+":
                        stack.append(a + b)
                    if token == "-":
                        stack.append(b - a)
                    if token == "*":
                        stack.append(a * b)
                    if token == "/":
                        stack.append(int(b / a))
                else:
                    return False

        return stack[-1]







