class Solution:
    
    def __init__(self):
        self.time = 1
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        def dfs(currNode, parent, disc, visited):
            
            visited[currNode] = True
            disc[currNode] = self.time
            low[currNode] = self.time
            self.time += 1
            
            for nbr in graph[currNode]:
                if nbr == parent:
                    continue
                
                if visited[nbr] == False:
                    dfs(nbr, currNode, disc, visited)
                
                low[currNode] = min(low[currNode], low[nbr])
                
                if disc[currNode] < low[nbr]:   #means there is no back-edge
                    ans.append([currNode, nbr])
            
        
        
        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
                
            
        visited = [False]*n
        disc = [0]*n  # discovery time
        low = [0]*n   # lowest discovery time of a back-edge
        
        ans = []
        for i in range(n):
	       if visited[i] == False:
                dfs(i, -1, disc, visited)
        
        return ans
