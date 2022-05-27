class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        
        '''
        
        indegree = []
        outdegree = []
        
        '''
        
        indegree = [0]*(1 + n)
        outdegree = [0]*(1 + n)
        
        
        for x, y in trust:
            outdegree[x] += 1
            indegree[y] += 1
        
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        
        return -1
