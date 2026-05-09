class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones) # largest
            y = -heapq.heappop(stones) # 2nd largest
            if  (x - y) > 0:
                heapq.heappush(stones, - (x - y ) )

        return -stones[0] if stones else 0