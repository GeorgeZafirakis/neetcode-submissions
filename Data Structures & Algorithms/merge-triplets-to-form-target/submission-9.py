class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        validSet = set()

        for triplet in triplets:

            
            # invalid triplet
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue 
            
            if triplet[0] == target[0]:
                validSet.add(0)

            if triplet[1] == target[1]:
                validSet.add(1)

            if triplet[2] == target[2]:
                validSet.add(2)    

        return len(validSet) == 3

                