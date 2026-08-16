class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = 1
        buf = []
        for i in range(len(digits)):
            curDigit = 10 ** (len(digits) - 1 - i) * int(digits[i])
            res += curDigit
            
        res = str(res)
        for c in res:
            buf.append(c)

        return buf