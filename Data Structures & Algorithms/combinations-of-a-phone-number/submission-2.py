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

        def dfs(i, subset):

            # Base Case
            if i == len(digits):
                res.append("".join(subset))
                return

            # Recursive Case
            letters = digitToChar[digits[i]]
            for letter in letters:
                subset.append(letter)
                dfs(i+1, subset)
                subset.pop()



        dfs(0,[])
        return res