class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, source, destination):
        self.add_vertex(source)
        self.add_vertex(destination)

        self.graph[source].append(destination)
        # self.graph[destination].append(source)

    def display(self):
        for vertex in self.graph:
            print(vertex, "  -> ", self.graph[vertex])

graph = DirectedGraph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("D", "E")

graph.display()
