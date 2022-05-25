class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        INT_MAX = 10**8
        distance = [[INT_MAX for j in range(k + 2)] for i in range(n)]
        distance[src][k + 1] = 0
        
        graph = defaultdict(list)
        for x, y, cost in flights:
            graph[x].append((y, cost))
            
        
        heap = []
        heapq.heapify(heap)
        
        heapq.heappush(heap, (0, k + 1, src))
        
        while len(heap) > 0:
            current_cost, stops, city = heapq.heappop(heap)
            
            if city == dst:
                return current_cost
            
            if stops == 0:
                continue
            
            for neighbour, travel_cost in graph[city]:
                new_cost = current_cost + travel_cost
                
                if distance[neighbour][stops - 1] > new_cost:
                    distance[neighbour][stops - 1] = new_cost
                    heapq.heappush(heap, (new_cost, stops - 1, neighbour))
            
            
        
        return -1
        
        '''
        
            0      1    2
        0   inf   inf   0
        1   inf   100
        2   200   inf
        3   600   inf
        
        dist[city][k] means the cost to react city with k stops in hand
        queue = [(100, 1, 0)]
        
        
        '''
