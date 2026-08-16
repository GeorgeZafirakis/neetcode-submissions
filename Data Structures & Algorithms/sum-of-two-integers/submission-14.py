class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to keep only 32 bits
        mask = 0xFFFFFFFF
        
        res = 0
        carry = 0
        
        for i in range(32):
            a_bit   = (a >> i) & 1
            b_bit   = (b >> i) & 1
            cur_bit = (a_bit ^ b_bit) ^ carry
            carry   = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)
            
            if cur_bit:
                res = res | (1 << i)
        
        # Handle negative numbers (convert from 32-bit representation)
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        
        return res