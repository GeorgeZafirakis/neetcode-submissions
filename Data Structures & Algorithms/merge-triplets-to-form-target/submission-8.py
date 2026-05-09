class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        validTriplets = []
        flags = [False] * 3

        for triplet in triplets:
            
            if (triplet[0] > target[0] or
                triplet[1] > target[1] or
                triplet[2] > target[2]):
                continue
            else:
                validTriplets.append(triplet)

        for triplet in validTriplets:

            if (triplet[0] == target[0]):
                flags[0] = True   

            if (triplet[1] == target[1]):
                flags[1] = True

            if (triplet[2] == target[2]):
                flags[2] = True

        for flag in flags:
            if flag == False:
                return False
        return True