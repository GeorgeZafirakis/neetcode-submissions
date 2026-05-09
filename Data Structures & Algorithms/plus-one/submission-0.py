class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        r = 0
        for i, n in enumerate(digits):
            r += n * 10**(len(digits) - i - 1)
        r += 1

        st = str(r)
        res = []
        
        for c in st:
            res.append(int(c))

        return res