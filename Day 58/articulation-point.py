from collections import defaultdict

class Solution:

    def __init__(self):
        self.time = 0

    def dfs(self, graph, currNode, parentNode, visited, low, disc, ap):
        visited[currNode] = True
        disc[currNode] = self.time
        low[currNode] = self.time
        self.time += 1
        children = 0

        for nbr in graph[currNode]:
            
            if nbr == parentNode:
                continue
            
            if not visited[nbr]:
                
                children += 1
                self.dfs(graph, nbr, currNode, visited, low, disc, ap)
                low[currNode] = min(low[currNode], low[nbr])

                if parentNode == -1 and children > 1:   
                    ap.append(currNode)
                if parentNode != -1 and disc[currNode] <= low[nbr]:
                    ap.append(currNode)

            else:
                low[currNode] = min(low[currNode], disc[nbr])

    def articulationPoints(self, n: int, connections):
        # Initialize graph
        graph = defaultdict(list)

        # Add edges
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)

        # Initialize other variables that are required
	   
        visited = [False]*n
        disc = [0]*n   #discovery time
        low = [0]*n    #lowest discovery time of back-edge
        ap = []

        # Call DFS
        for currNode in range(n):
            if not visited[currNode]:
                parentNode = -1
                self.dfs(graph, currNode, parentNode, visited, low, disc, ap)

        return ap


obj = Solution()
connections = [[0,2],[2,1],[0,1],[1,3],[3,5],[5,4],[4,1]]
print(obj.articulationPoints(6, connections))

