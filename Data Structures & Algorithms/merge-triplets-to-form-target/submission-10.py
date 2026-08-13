class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        flags = [False] * (3)

        for triplet in triplets:

            if (triplet[0] > target[0] or 
                triplet[1] > target[1] or 
                triplet[2] > target[2]):
                continue

            if triplet[0] == target[0]: flags[0] = True
            if triplet[1] == target[1]: flags[1] = True
            if triplet[2] == target[2]: flags[2] = True

        return True if not False in flags else False