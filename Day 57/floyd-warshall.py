from sqlite3 import connect


def floydWarshall(n : int, connections: list[list[int]]):
    INT_MAX = 10**8
    dp = [[INT_MAX for j in range(n)] for i in range(n)]

    for x, y, cost in connections:
        dp[x][y] = cost
        dp[x][x] = 0
        dp[y][y] = 0

    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    
    print(dp)
    return dp
    
    
connections = [[0, 3, 10], [0 ,1 ,5], [1, 2, 3], [2, 3, 1]]
n = 4
floydWarshall(n, connections)