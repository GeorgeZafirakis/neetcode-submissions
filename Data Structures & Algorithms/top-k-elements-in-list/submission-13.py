class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myMap = defaultdict(int)
        for num in nums:
            myMap[num] = 1 + myMap.get(num, 0)
        
        counterList = []
        myInversedMap = defaultdict(list)
        
        for num, counter in myMap.items():
            myInversedMap[counter].append(num)
            counterList.append(counter)
        
        counterList = list(set(counterList))  # remove duplicates
        counterList.sort(reverse=True)        # sort descending
        
        res = []
        for freq in counterList:
            for num in myInversedMap[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         myMap = defaultdict(list)
#         for num in nums:
#             myMap[num] = 1 + myMap.get(myMap[num], 0)
        
#         counterList = []
#         myInversedMap = defaultdict(list)
#         for num, counter in myMap.items():
#             myInversedMap[counter] = num
#             counterList.append(counter)
        
#         counterList.sort()
#         counterList.reverse

#         res = []
#         for i in range(0, 1, k):
#             res.appendmyInversedMap(counterList(i))
#         return res