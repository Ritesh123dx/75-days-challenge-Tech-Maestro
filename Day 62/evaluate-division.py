class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        graph = defaultdict(list)
        
        n = len(equations)
        for i in range(n):
            x, y = equations[i]
            val = values[i]
            
            graph[x].append((y, val))
            graph[y].append((x, 1/val))
        
        ans = []
        
        for i in range(len(queries)):
            x, y = queries[i]
            
            
            if x not in graph or y not in graph:
                ans.append(-1)
                continue
                

            queue = deque()
            queue.append((x, 1))
            visited = set()
            visited.add(x)
            
            while len(queue) > 0:
                
                node, val = queue.popleft()
                if node == y:
                    ans.append(val)
                    break
                
                for nbr, v in graph[node]:
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append((nbr, val*v))
            
            
            if len(ans) == i:
                ans.append(-1)
                
        
        return ans
                
            
            