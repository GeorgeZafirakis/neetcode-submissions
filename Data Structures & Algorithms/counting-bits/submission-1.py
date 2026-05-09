class Solution:
    def countBits(self, n: int) -> List[int]:

        def helper(n: int) -> int:
            res = 0
            for i in range(32):
                if n % 2 == 1:
                    res += 1
                n = n >> 1
            return res

        res = []
        for i in range(n+1):
            res.append(helper(i))
        return res

        