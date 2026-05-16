class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n     = len(s)
        dp    = [False] * (n+1)
        dp[n] = True

        for i in range(n-1,-1,-1):
            
            for w in wordDict:

                if dp[i] == True:
                    continue
                
                if i + len(w) <= n and w == s[i:i+len(w)]:
                    dp[i] = dp[i + len(w)]

        return dp[0]