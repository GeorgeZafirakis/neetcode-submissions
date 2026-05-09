class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        good = set()
        
        for triplet in triplets:

            # Skip triplets with an element larger than target at position i -> 0...2
            if (triplet[0] > target[0]
            or  triplet[1] > target[1]
            or  triplet[2] > target[2]):
                continue

            for i, v in enumerate(triplet):
                if v == target[i]:
                    good.add(i)

        return len(good) == 3

            

        