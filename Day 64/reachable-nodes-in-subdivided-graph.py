class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        
        '''
        1. Perform Dijktstra to reach the number of nodes in shortest path.
        2. Calculate the movesLeft for each valid node that can be reached from source (node 0). Also count these valid nodes
        
        3. next calculate the sub-divided nodes between the two edges.
            
            if movesLeft[x] + movesLeft[y] > cnt:
                means it can be covered entirely
            else:
                only (movesLeft[x] + movesLeft[y]) nodes can be convered.
            
            Min of (movesLeft[x] + movesLeft[y], cnt)
        
        '''
        
        graph = defaultdict(list)
        for x, y, cnt in edges:
            graph[x].append((y, cnt + 1))
            graph[y].append((x, cnt + 1))
            
        INT_MAX = 10**8
        dist = [INT_MAX]*n
        dist[0] = 0
        heap = [(0, 0)]
        
        #Performing Dijkstra's
        while len(heap) > 0:
            d, node = heapq.heappop(heap)
            
            for nbr, w in graph[node]:
                if d + w < dist[nbr]:
                    dist[nbr] = d + w
                    heapq.heappush(heap, (d + w, nbr))
        
        
        movesLeft = [0]*n
        nodesReached = 0
        
        #Counting valid nodes that can be reached and updating movesLeft list.
        for node in range(n):
            if dist[node] <= maxMoves:
                nodesReached += 1
                movesLeft[node] = maxMoves - dist[node]
        
        
        #Counting the sub-divided nodes that can be reached.
        for x, y, cnt in edges:
            nodesReached += min(movesLeft[x] + movesLeft[y], cnt)
        
        
        return nodesReached
        
        
