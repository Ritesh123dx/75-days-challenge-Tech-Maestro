class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)
        
        self.size = 0
        

    def addNum(self, num: int) -> None:
        if self.size%2 == 0:
            heapq.heappush( self.maxheap, -1*num ) 
        else:
            heapq.heappush( self.minheap, num )
        
        
        if len(self.minheap) > 0 and -1*self.maxheap[0] > self.minheap[0]:

            val1 = -1*heapq.heappop( self.maxheap )
            val2 = heapq.heappop( self.minheap )

            heapq.heappush(self.minheap, val1)
            heapq.heappush(self.maxheap, -1*val2)

        
        self.size += 1

    def findMedian(self) -> float:
        
        if self.size%2 == 0:
            val1 = -1*self.maxheap[0]
            val2 = self.minheap[0]
            
            return (val1 + val2)/2
        
        else:
            return -1*self.maxheap[0]
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
