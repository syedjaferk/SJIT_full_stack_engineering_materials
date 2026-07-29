class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex_1, vertex_2):
        self.add_vertex(vertex_1)
        self.add_vertex(vertex_2)

        self.graph[vertex_1].append(vertex_2)
        self.graph[vertex_2].append(vertex_1)

    def display(self):
        for vertex in self.graph:
            print(vertex, "  -> ", self.graph[vertex])

graph = UndirectedGraph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("D", "E")

graph.display()
