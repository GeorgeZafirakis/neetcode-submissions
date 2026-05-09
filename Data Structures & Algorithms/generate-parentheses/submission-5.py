class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def dfs(i, curList, openN, closedN):
            
            # Base Case
            if i == 2*n and openN == closedN:
                res.append("".join(curList.copy()))
                return

            if i > 2*n or openN < closedN:
                return

            # Recursive Case
            if openN < n:
                curList.append("(")
                dfs(i+1, curList, openN + 1, closedN)
                curList.pop()

            if closedN < openN:
                curList.append(")")
                dfs(i+1, curList, openN, closedN + 1)
                curList.pop()


        dfs(0,[], 0, 0)
        return res