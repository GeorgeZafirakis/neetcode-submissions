class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        
        def dfs(subset, openN, closedN):

            # Base Case
            if openN == closedN == n:
                res.append("".join(subset.copy()))
                return

            # Recursive Case
            if openN < n:
                subset.append("(")
                openN += 1
                dfs(subset, openN, closedN)
                subset.pop()
                openN -= 1


            if closedN < openN:
                subset.append(")")
                closedN += 1
                dfs(subset, openN, closedN)
                subset.pop()
                closedN -= 1

        dfs([], 0, 0)
        return res


        