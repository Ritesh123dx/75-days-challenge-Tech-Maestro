class MedianHeap:
    
    def __init__(self):
        self.minheap = []
        self.maxheap = []
        
    
    def add(self, val):
        if len(self.maxheap) <= len(self.minheap):
            heapq.heappush(self.maxheap, -val)
        else:
            heapq.heappush(self.minheap, val)
        
        
        
        if len(self.minheap) > 0 and self.minheap[0] < -self.maxheap[0]:
            val1 = heapq.heappop(self.minheap)
            val2 = -heapq.heappop(self.maxheap)
            
            heapq.heappush(self.maxheap, -val1)
            heapq.heappush(self.minheap, val2)
            
    
    def remove(self, val):
        if val in self.minheap:
            self.minheap.remove(val)
            heapq.heapify(self.minheap)
        else:
            self.maxheap.remove(-val)
            heapq.heapify(self.maxheap)
        
        
        
    
    def getMedian(self):
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + -1*self.maxheap[0] )/2
        else:
            return -self.maxheap[0]


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        heap = MedianHeap()
        
        l = 0
        r = 0
        n = len(nums)
        ans = []
        
        
        while r < n:
            heap.add(nums[r])
            
            if r < k - 1:
                r += 1
                continue
            
            ans.append(heap.getMedian())
            
            heap.remove(nums[l])
            
            l += 1
            r += 1
        
        
        return ans
        
        
