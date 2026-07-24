class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(openN, closedN, subSet):
        
            # Base Case
            if openN == closedN == n:
                res.append("".join(subSet.copy()))
                return

            if closedN > openN or openN > n:
                return

            # Recursive Case
            if openN < n:
                subSet.append("(")
                dfs(openN+1,closedN, subSet)
                subSet.pop()
                
            if closedN < openN:
                subSet.append(")")
                dfs(openN,closedN+1, subSet)
                subSet.pop()   


        dfs(0,0,[])
        return res