class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        for stone in stones:
            heap.append(-stone)
        
        heapq.heapify(heap)
        
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            
            first = first - second
            
            if first > 0:
                heapq.heappush(heap, -first)
        
        if len(heap) == 0:
            return 0
        else:
            return -heapq.heappop(heap)
