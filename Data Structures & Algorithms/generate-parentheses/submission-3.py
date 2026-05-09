class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(subset, openN, closedN):

            # Base Case
            if openN == closedN == n:
                res.append("".join(subset))
                return

            # Recursive Case
            if openN < n:
                subset.append("(")
                dfs(subset, openN + 1, closedN)
                subset.pop()

            if closedN < openN:
                subset.append(")")
                dfs(subset, openN, closedN + 1)
                subset.pop()


        dfs([],0,0)
        return res