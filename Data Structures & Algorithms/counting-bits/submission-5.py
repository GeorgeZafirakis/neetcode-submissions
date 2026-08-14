class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []
        for num in range(n+1):
            res.append(self.helper(num))
        return res

    def helper(self, n: int) -> int:

        counter = 0
        while n:
            counter += n &  1
            n       =  n >> 1
        return counter
