class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i,curList):

            # Base Case
            if i >= len(digits):
                res.append("".join(curList.copy()))
                return

            # Recursive Case
            digit = digits[i]
            for c in digitToChar[digit]:
                curList.append(c)
                dfs(i+1,curList)
                curList.pop()

        dfs(0,[])
        return res