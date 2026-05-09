class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []
        for num in range(n+1):
            counter = 0
            for i in range(32):
                if num & (1 << i):
                    counter += 1
            res.append(counter)
        return res