class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        myMap = {}
        for num in nums:
            if num in myMap:
                myMap[num] += 1
            else:
                myMap[num] = 1
        
        count = 0
        for t in myMap:
            count = max(count, myMap[t])

        for res in myMap:
            if myMap[res] == count:
                return res
        return -1