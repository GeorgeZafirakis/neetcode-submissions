class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def dfs(i,subset,open,close):

            # Base Case
            if i == 2*n and open == close:
                res.append("".join(subset))
                return

            if close > open:
                return

            if i > 2*n:
                return

            # Recursive Case
            if open < n:
                subset.append("(")
                dfs(i+1,subset,open+1,close)
                subset.pop()

            if close < n:
                subset.append(")")
                dfs(i+1,subset,open,close+1)
                subset.pop()

        dfs(0,[],0,0)
        return res

        