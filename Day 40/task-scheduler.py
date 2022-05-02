class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        hashmap = defaultdict(int)
        for task in tasks:
            hashmap[task] += 1
        
        heap = []
        heapq.heapify(heap)
        
        for task in hashmap:
            heapq.heappush(heap, -hashmap[task] )
        
        time = 0
        
        while len(heap) > 0:
            temp = []
            tasks_processed = 0
            
            while len(heap) > 0 and tasks_processed <= n:
                count = -heapq.heappop(heap)
                
                count -= 1
                
                if count > 0:
                    temp.append(count)
                
                tasks_processed += 1
            
            
            if len(temp) == 0:
                time += tasks_processed
            else:
                time += n + 1
                
                for count in temp:
                    heapq.heappush(heap, -count)
        
        
        return time
            
            
            
                
            
