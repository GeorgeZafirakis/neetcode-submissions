class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []

        for point in points:
            distance = -(point[0]*point[0] + point[1]*point[1])
            heapq.heappush(res, [distance, point])
            if len(res) > k:
                heapq.heappop(res)

        return [ k[1] for k in res ]
