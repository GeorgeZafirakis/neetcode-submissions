class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        myMap = {}
        for num in nums:
            if num in myMap:
                myMap[num] = 1 + myMap[num]
            else:
                myMap[num] = 1

        (n, t) = (-1, -1)
        for num in myMap:
            if myMap[num] > t:
                (n, t) = (num, myMap[num]) 
        return n