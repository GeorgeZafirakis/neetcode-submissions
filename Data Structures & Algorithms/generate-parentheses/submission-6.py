class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        
        def dfs(curList, openN, closedN):

            # Base Case
            if openN == closedN == n:
                res.append("".join(curList.copy()))
                return

            if openN > n or closedN > n:
                return

            # Recursive Case
            if openN < n:
                curList.append("(")
                dfs(curList, openN+1, closedN)
                curList.pop()

            if closedN < openN:
                curList.append(")")
                dfs(curList, openN, closedN+1)
                curList.pop()


        dfs([], 0, 0)
        return res