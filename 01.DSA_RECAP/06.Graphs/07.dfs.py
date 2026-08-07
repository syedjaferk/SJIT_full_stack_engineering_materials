graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

def dfs(graph, node, visited):
    if node is visited:
        return

    print(node)
    visited.add(node)

    for neighbour in graph.get(node, []):
        dfs(graph, neighbour, visited)

visited = set()
dfs(graph, "A", visited)
