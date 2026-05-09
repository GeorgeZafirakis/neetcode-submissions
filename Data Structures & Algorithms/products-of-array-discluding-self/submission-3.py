class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        cnt_zeros = 0
        
        # Find prod of all elements and count zeros
        for num in nums:
            if num:
                prod *= num
            else:
                cnt_zeros += 1

        res = [0] * len(nums)

        # If more than 2 zeros in list, all zeros
        if cnt_zeros >= 2:
            return res

        for i, num in enumerate(nums):
            if cnt_zeros:
                if num == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod // num
        return res

        
