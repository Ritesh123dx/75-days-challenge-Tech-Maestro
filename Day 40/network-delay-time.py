class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for x, y, t in times:
            graph[x].append((y, t))
        
        
        heap = [(0, k)]
        heapq.heapify(heap)
        delay = [10**8]*(1 + n)
        delay[k] = 0
        
        
        while len(heap) > 0:
            arrival_time, node = heapq.heappop(heap)
            
            for child, time in graph[node]:
                if arrival_time + time < delay[child]:
                    delay[child] = arrival_time + time
                    heapq.heappush(heap, (arrival_time + time, child))
        
        
        ans = 0
        for i in range(1, n + 1):
            if delay[i] == 10**8:
                return -1
            
            ans = max(ans, delay[i])
        
        return ans
                    
            
