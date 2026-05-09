class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c   == '(': stack.append(")")
            elif c == '{': stack.append("}")
            elif c == '[': stack.append("]")
            elif len(stack) == 0: return False
            elif stack.pop() != c: return False
        
        return len(stack) == 0  # Fixed: should return True if stack is empty
