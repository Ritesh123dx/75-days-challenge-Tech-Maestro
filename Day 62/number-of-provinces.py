class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def bfs(isConnected : list[list[int]], vertex : int, visited : list[bool]) -> None:
            queue = deque()
            visited[vertex] = True
            queue.append(vertex)
            
            while len(queue) > 0:
                
                for i in range(len(queue)):
                    node = queue.popleft()
                    
                    for nbr in range(len(isConnected[node])):
                        if nbr == node or visited[nbr] or isConnected[node][nbr] == 0:
                            continue
                        
                        queue.append(nbr)
                        visited[nbr] = True
        
        
        
        n = len(isConnected)
        visited = [False]*n
        count = 0
        
        for i in range(n):
            if visited[i] == False:
                bfs(isConnected, i, visited)
                count += 1
        
        return count
            