class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = []
        # O(n) time complexity
        for stone in stones:
            maxHeap.append(-stone)

        # O(n) time complexity
        heapq.heapify(maxHeap)

        # O(n) for the loop
        while len(maxHeap) > 1:
            # O(nlogn) for pop and push
            s1 = heapq.heappop(maxHeap)
            s2 = heapq.heappop(maxHeap)
            if s1 != s2:
                heapq.heappush(maxHeap, s1 - s2)

        return -maxHeap[0] if maxHeap else 0