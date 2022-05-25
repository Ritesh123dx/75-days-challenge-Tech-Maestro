class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        
        graph = defaultdict(list)
        
        for i in range(n):
            for nbr in rooms[i]:
                graph[i].append(nbr)
        
        
        visited = [False]*n
        visited[0] = True
        
        queue = deque()
        queue.append(0)
        
        
        while len(queue) > 0:
            for i in range(len(queue)):
                room = queue.popleft()
                
                for nbr in graph[room]:
                    if visited[nbr] == False:
                        visited[nbr] = True
                        queue.append(nbr)
        
        
        for val in visited:
            if val == False:
                return False
        
        return True
