
from math import dist
from operator import ne
from xxlimited import new


graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("D", 3)],
    "C": [("A", 2), ("D", 1)],
    "D": [("C",1), ("B", 3)]
}

def dijkistras(graph, source):
    distances = {}

    for node in graph:
        distances[node] = float("inf")

    distances[source] = 0
    visited = set()

    while len(visited) < len(graph):
        current = None

        for node in graph:
            if node in visited:
                continue

            if current is None or distances[node] < distances[current]:
                current = node
        print("#"*10)
        print("Current Node : ", current)

        visited.add(current)

        for neighbor, weight in graph[current]:
            print("Neighbor ", neighbor)
            new_distance = distances[current] + weight
            print(f"Distance from {current}")
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
    return distances

result = dijkistras(graph, "A")
print(result)
