class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPali(s: str) -> bool:

            if not s: return True
            l, r = 0, len(s) - 1
            
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        res = []
        def dfs(i,curList):

            # Base Case
            if i == len(s):
                res.append(curList.copy())
                return

            # Recursive Case
            for j in range(i, len(s)):

                chunk = s[i:j+1]
                if isPali(chunk):
                    curList.append(chunk)
                    dfs(j+1,curList)
                    curList.pop()
                    


        dfs(0,[])
        return res

