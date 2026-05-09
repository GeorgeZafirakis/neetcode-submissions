class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        maxHeap = []
        for num in maxHeap:
            heapq.heappush(minHeap, -num)

        return minHeap[0]