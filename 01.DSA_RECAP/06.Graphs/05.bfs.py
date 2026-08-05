from collections import deque
from operator import ne

graph = [
    [0,1,1,0,0,0],
    [1,0,0,1,1,0],
    [1,0,0,0,0,0],
    [0,1,0,0,0,0],
    [0,1,0,0,0,0],
    [0,0,0,0,0,0]
]

vertices = ["A", "B", "C", "D", "E", "F"]

def bfs(graph, start, destination):
    visited = [False] * len(graph)
    queue = deque()
    visited[start] = True
    queue.append(start)

    while queue:
        current = queue.popleft()

        # if destination is reached
        if current == destination:
            print("Destination Reached")
            break

        for neighbour in range(len(graph[current])):
            if graph[current][neighbour] == 1 and not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

bfs(graph, 1, 5)
