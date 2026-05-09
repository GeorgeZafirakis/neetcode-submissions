class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        revSign = [-s for s in stones]
        heapq.heapify(revSign)
        maxHeap = revSign
        
        while len(maxHeap) > 1:
            s1 = heapq.heappop(maxHeap)
            s2 = heapq.heappop(maxHeap)

            if s1 == s2: 
                continue
            else:
                s = s1 - s2
                heapq.heappush(maxHeap, s)

        return -maxHeap[0] if maxHeap else 0