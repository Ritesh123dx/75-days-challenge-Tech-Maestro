from collections import defaultdict

def dfs1(vertex : int, visited : list[bool], stack : list[int], graph : dict[int, int]):

    visited[vertex] = True

    for nbr in graph[vertex]:
        if visited[nbr] == False:
            dfs1(nbr, visited, stack, graph)
    
    stack.append(vertex)


def getReversedGraph(connections : list[list[int]]):
    graph = defaultdict(list)

    for x, y in connections:
        graph[y].append(x)

    return graph


def dfs2(vertex : int, visited : list[bool], graph : dict[int, int]):
    visited[vertex] = True
    print(vertex)

    for nbr in graph[vertex]:
        if visited[nbr] == False:
            dfs2(nbr, visited, graph)


def noOfSSC(n : int, connections: list[list[int]]):
    graph = defaultdict(list)

    for x, y in connections:
        graph[x].append(y)

    
    stack = []
    visited = [False]*n

    for vertex in range(n):
        if visited[vertex] == False:
            dfs1(vertex, visited, stack, graph)


    reversed_graph = getReversedGraph(connections)

    visited = [False]*n
    while len(stack) > 0:
        vertex = stack.pop()

        if visited[vertex] == False:
            print("Component : ")
            dfs2(vertex, visited, reversed_graph)


