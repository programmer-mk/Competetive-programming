
from collections import deque

def dfs(graph):
    visited = [False for _ in graph]
    stack = []
    stack.append(1)
    while len(stack):
        node  = stack.pop()
        if not visited[node-1]:
            visited[node-1] = True
            print(node)
            for neighbor in graph[node]:
                if not visited[neighbor-1]:
                    stack.append(neighbor)


def bfs(graph):
    visited = [False for _ in graph]
    queue = deque()
    queue.appendleft(1)
    while len(queue):
        node = queue.popleft()
        if not visited[node-1]:
            visited[node-1] = True
            print(node)
            for neighbor in graph[node]:
                if not visited[neighbor-1]:
                    queue.appendleft(neighbor)



def build_graph(edges):
    graph = {}
    for edge in edges:
        if graph.get(edge[0]):
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]

        if not graph.get(edge[1]):
            graph[edge[1]] = []

    return graph



graph = build_graph([[1, 2], [1, 3], [3, 4], [3, 2], [2, 4]])
#bfs(graph)
dfs(graph)
