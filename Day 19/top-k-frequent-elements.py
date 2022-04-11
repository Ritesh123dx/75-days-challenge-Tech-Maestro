class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        
        heap = []
        heapq.heapify(heap)
        
        for num in hashmap.keys():
            freq = hashmap[num]
            heapq.heappush(heap, (freq, num))
            
            while len(heap) > k:
                heapq.heappop(heap)
        
        
        ans = []
        while len(heap) > 0:
            freq, num = heapq.heappop(heap)
            ans.append(num)
            
            
        return ans
            
        
