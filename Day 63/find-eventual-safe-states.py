class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        
        def dfs(vertex, visited, visiting, dp):
            
            if dp[vertex] != -1:
                return dp[vertex]
            
            visiting[vertex] = True
            
            for nbr in graph[vertex]:
                if visiting[nbr] == True:
                    dp[vertex] = 0
                    return False
                
                if dfs(nbr, visited, visiting, dp) == False:
                    dp[vertex] = 0
                    return False
            
            
            visiting[vertex] = False
            visited[vertex] = True
            
            dp[vertex] = 1
            return True
        
        
        n = len(graph)
        visited = [False]*n
        visiting = [False]*n
        dp = [-1]*n
        ans = []
        
        for vertex in range(n):
            if visited[vertex] == False:
                dfs(vertex, visited, visiting, dp)
            
            if dp[vertex] == 1:
                ans.append(vertex)
        
        
        return ans
        
        
            
            
