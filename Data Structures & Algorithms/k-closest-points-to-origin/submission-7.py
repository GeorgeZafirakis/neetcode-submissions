class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxHeap = []
#        heapq.heapify(maxHeap)

        for x,y in points:
            dist = x*x + y*y
            heapq.heappush(maxHeap, (-dist,[x,y]))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [point for (dist,point) in maxHeap]

        
