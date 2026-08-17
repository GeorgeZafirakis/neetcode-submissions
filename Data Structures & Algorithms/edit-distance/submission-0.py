class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # word1 w
        #       o
        #       r
        #       d
        #       2
        
        n1,n2 = len(word1), len(word2)
        dp    = [ [0] * (n1 + 1) for _ in range(n2 + 1) ]

        for i in range(n2,-1,-1):
            dp[n2-i][n1] = i

        for i in range(n1,-1,-1):
            dp[n2][n1-i] = i

        for y in range(n2-1,-1,-1):
            for x in range(n1-1,-1,-1):

                if word2[y] == word1[x]:
                    dp[y][x] = dp[y+1][x+1]
                else:
                    dp[y][x] = 1 + min(
                        dp[y+1][x],
                        dp[y][x+1],
                        dp[y+1][x+1]
                    )

        print(dp)
        return dp[0][0]

         