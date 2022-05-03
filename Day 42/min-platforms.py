import heapq

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        
        nums = []
        for i in range(n):
            nums.append([arr[i], dep[i]])
        
        
        nums.sort()
        minHeap = []
        heapq.heapify(minHeap)
        ans = 0
        
        for i in range(n):
            a, d = nums[i]
            
            while len(minHeap) > 0 and a > minHeap[0]:
                heapq.heappop(minHeap)
            
            heapq.heappush(minHeap, d)
            
            ans = max(ans, len(minHeap))
        
        
        return ans
