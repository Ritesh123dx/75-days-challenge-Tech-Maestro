class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if len(edges) == 0:
            return [0]
        
        graph = defaultdict(set)
        indegree = [0]*n
        
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
            indegree[x] += 1
            indegree[y] += 1
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
        
        while n > 2:
            
            for i in range(len(queue)):
                
                node = queue.popleft()

                for nbr in graph[node]:
                    graph[nbr].remove(node)
                    indegree[nbr] -= 1

                    if indegree[nbr] == 1:
                        queue.append(nbr)

                n -= 1
        
        
        return list(queue)
        
