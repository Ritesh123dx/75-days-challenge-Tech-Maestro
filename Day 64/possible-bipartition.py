class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        def bfs(queue, colors):
            
            while len(queue) > 0:
                n = len(queue)
                for i in range(n):
                    node, color = queue.popleft()
                    
                    for child in graph[node]:
                        if colors[child] == color:
                            return False
                        
                        if colors[child] == -1:
                            colors[child] = 1 - color
                            queue.append((child, 1 - color))
            
            return True
        
        
        graph = defaultdict(list)
        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        
        colors = [-1]*(n + 1)
        queue = deque()
        
        for i in range(1, n + 1):
            if colors[i] == -1:
                queue.append((i, 0))
                colors[i] = 0
                if bfs(queue, colors) == False:
                    return False
        
        return True
