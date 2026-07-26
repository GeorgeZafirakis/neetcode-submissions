class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        myMap = {}

        for num in nums:

            if num in myMap:
                counter    = myMap[num]
                myMap[num] = counter + 1
            else:
                myMap[num] = 1

        arr = []
        for num, cnt in myMap.items():
            arr.append([cnt,num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
