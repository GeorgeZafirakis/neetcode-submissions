class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        counterZero = 0
        counterOne  = 0
        counterTwo  = 0

        # Count
        for num in nums:
            if num == 0:
                counterZero += 1
            elif num == 1:
                counterOne += 1
            else:
                counterTwo += 1

        i = 0

        # Place 0s
        while counterZero > 0:
            nums[i] = 0
            i += 1
            counterZero -= 1

        # Place 1s
        while counterOne > 0:
            nums[i] = 1
            i += 1
            counterOne -= 1

        # Place 2s
        while counterTwo > 0:
            nums[i] = 2
            i += 1
            counterTwo -= 1