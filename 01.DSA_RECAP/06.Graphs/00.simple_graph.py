class Graph:
    def __init__(self):
        self.vertices = [] # Nodes
        self.edges = [] # Connections between nodes

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)

    def add_edge(self, vertex_1, vertex_2):
        self.edges.append((vertex_1, vertex_2))

    def display(self):
        print("Vertices ", self.vertices)
        print("Edges ", self.edges)


graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")

graph.add_edge("A", "B")
graph.add_edge("A", "C")

graph.display()
