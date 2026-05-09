class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(l1,l2):
            return -((l1[0] - l2[0])*(l1[0] - l2[0]) + (l1[1] - l2[1])*(l1[1] - l2[1]))

        maxHeap = []
        heapq.heapify(maxHeap)

        for point in points:
            heapq.heappush(maxHeap, (dist(point,[0,0]),point))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        for (dist,p) in maxHeap:
            res.append(p)
        return res

        
