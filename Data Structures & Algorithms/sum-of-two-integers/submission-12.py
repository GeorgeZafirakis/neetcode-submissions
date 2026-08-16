class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to keep only 32 bits
        mask = 0xFFFFFFFF
        
        # Convert to 32-bit (handle negative numbers in Python)
        a = a & mask
        b = b & mask
        
        res = 0
        carry = 0
        
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur_bit = (a_bit ^ b_bit) ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            
            if cur_bit:
                res = res | (1 << i)
        
        # Handle negative numbers (convert from 32-bit representation)
        res = res & mask
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        
        return res