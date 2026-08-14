class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        res   = []
        myMap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def dfs(i, curList):

            if i == len(digits):
                res.append("".join(curList))
                return

            if i > len(digits):
                return 

            for c in myMap[digits[i]]:
                curList.append(c)
                dfs(i+1,curList)
                curList.pop()

        dfs(0,[])
        return res


                