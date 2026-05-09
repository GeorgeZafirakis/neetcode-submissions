class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if len(trust) == 1:
            return trust[0][1]

        res = -1
        for i in range(len(trust) - 1):
            p1 = trust[i][1]
            p2 = trust[i+1][1]
            res = p1

            if p1 != p2:
                return -1

        return res
