class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        flags = [False] * 3
        
        for triplet in triplets:
            
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                flags[0] = True

            if triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]:
                flags[1] = True

            if triplet[2] == target[2] and triplet[0] <= target[0] and triplet[1] <= target[1]:
                flags[2] = True


        for res in flags:
            if res == False:
                return False
        return True

            