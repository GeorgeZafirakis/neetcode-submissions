class Solution:
    def getSum(self, a: int, b: int) -> int:

        carry = 0
        res = 0

        for i in range(32):
            d1 = (a >> i) & 1
            d2 = (b >> i) & 1

            if d1 and d2 and carry:
                c     = 1
                carry = 1
            elif d1 and d2:
                c = 0
                carry = 1
            elif (d1 or d2) and carry:
                c = 0
                carry = 1
            elif (d1 or d2):
                c = 1
                carry = 0
            elif carry:
                c = 1
                carry = 0
            else:
                c = 0
                carry = 0

            res |= ( c << i)

        # Convert to signed 32-bit integer
        if res >= 2**31:
            res -= 2**32

        return res

            
        