class WeightedUndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex_1, vertex_2, weight):
        self.add_vertex(vertex_1)
        self.add_vertex(vertex_2)

        self.graph[vertex_1].append((vertex_2, weight))
        self.graph[vertex_2].append((vertex_1, weight))

    def display(self):
        for vertex in self.graph:
            print(vertex, "  -> ", self.graph[vertex])

graph = WeightedUndirectedGraph()
graph.add_edge("A", "B", 2)
graph.add_edge("A", "C", 3)
graph.add_edge("B", "D", 4)
graph.add_edge("D", "E", 5)

graph.display()
