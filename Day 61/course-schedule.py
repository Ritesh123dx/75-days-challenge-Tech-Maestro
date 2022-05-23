class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        graph = defaultdict(list)
        
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        
        queue = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
        
        
        while len(queue) > 0:
            
            courseNum = queue.popleft()
            
            for nbr in graph[courseNum]:
                indegree[nbr] -= 1
                
                if indegree[nbr] == 0:
                    queue.append(nbr)
        
        
        return sum(indegree) == 0
            