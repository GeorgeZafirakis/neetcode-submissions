class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        myMap = {}

        for i in range(len(numbers)):

            diff = target - numbers[i]
            if diff in myMap:
                return [myMap[diff], i + 1]
            else:
                myMap[numbers[i]] = i + 1
        
        return []