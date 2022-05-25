class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def bfs(node, colors):
            queue = deque()
            queue.append((node, 0))
            colors[node] = 0
            
            while len(queue) > 0:
                qLen = len(queue)
                
                for i in range(qLen):
                    node, color = queue.popleft()
                    
                    for nbr in graph[node]:
                        if colors[nbr] == color:
                            return False
                        
                        elif colors[nbr] == -1:
                            colors[nbr] = 1 - color
                            queue.append((nbr, 1 - color))
                
            return True
        
        
        n = len(graph)
        colors = [-1]*n
        
        for i in range(n):
            if colors[i] == -1:
                if bfs(i, colors) == False:
                    return False
        
        return True
            
