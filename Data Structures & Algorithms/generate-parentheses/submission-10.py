class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        
        def dfs(openN, closedN, curList):

            if openN == closedN == n:
                res.append("".join(curList))
                return

            if openN > n or closedN > openN:
                return

            if n > openN:
                curList.append("(")
                dfs(openN+1,closedN,curList)
                curList.pop()

            if openN > closedN:
                curList.append(")")
                dfs(openN,closedN+1,curList)
                curList.pop()

        dfs(0,0,[])
        return res