class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def dfs(i,subSet):

            # Base Case
            if i == len(digits):
                res.append("".join(subSet.copy()))
                return

            # Recursive Case
            for c in digitToChar[digits[i]]:
                subSet.append(c)
                dfs(i+1,subSet)
                subSet.pop()

        dfs(0,[])
        return res




