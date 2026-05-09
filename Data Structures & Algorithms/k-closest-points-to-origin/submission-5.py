class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        buffer = []
        res = []
        
        # O(n) time
        for point in points:

            dist = point[0] * point[0] + point[1] * point[1]
            # O(1) time
            buffer.append([-dist, point])

        # O(n) time
        heapq.heapify(buffer)
        # O(n) time
        while len(buffer) > k:
            heapq.heappop(buffer)

        # O(n) time
        for dist, point in buffer:
            res.append(point)

        return res