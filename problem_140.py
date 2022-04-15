
from collections import deque

def topological_sort(n, edges):
    in_degree = {i: 0 for i in range(n)}
    graph = {i: [] for i in range(n)}
    result = []
    for edge in edges:
        graph[edge[0]].append(edge[1])
        in_degree[edge[1]] += 1

    queue = deque()
    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)

    while queue:
        target = queue.popleft()
        result.append(target)
        for neighbour in  graph[target]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)

    if len(result) != len(graph):
        return []
    else:
        return result


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))

main()