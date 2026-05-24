class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        
        def dfs(subSet,openN,closedN):

            # Base Case
            if n == openN == closedN:
                res.append("".join(subSet))
                return

            if closedN > openN:
                return

            # Recursive Case
            if openN < n:
                subSet.append("(")
                dfs(subSet,openN+1,closedN)
                subSet.pop()

            if openN > closedN:
                subSet.append(")")
                dfs(subSet,openN,closedN+1)
                subSet.pop()

        dfs([],0,0)
        return res