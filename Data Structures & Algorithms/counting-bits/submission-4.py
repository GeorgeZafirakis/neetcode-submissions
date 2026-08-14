class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def helper(n):

            counter = 0
            while n:
                counter += n &  1
                n       =  n >> 1
            return counter

        res = []
        for num in range(n+1):
            res.append(helper(num))
        return res
