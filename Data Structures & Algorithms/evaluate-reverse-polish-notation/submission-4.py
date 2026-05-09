class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        
        for token in tokens:
            if token in operators:
                d2 = stack.pop()
                d1 = stack.pop()
                
                if token == "+":
                    stack.append(d1 + d2)
                elif token == "-":
                    stack.append(d1 - d2)
                elif token == "*":
                    stack.append(d1 * d2)
                elif token == "/":
                    stack.append(int(d1 / d2))
            else:
                stack.append(int(token))
        
        return stack[0]