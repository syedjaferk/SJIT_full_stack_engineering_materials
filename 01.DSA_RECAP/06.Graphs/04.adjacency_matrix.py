class AdjacencyMatrix:

    def __init__(self, size) -> None:
        self.size = size
        self.matix = [[0]*size for _ in range(size)]

    def add_edge(self, v1, v2):
        self.matix[v1][v2] = 1
        self.matix[v2][v1] = 1

    def display(self):
        for row in self.matix:
            print(row)

graph = AdjacencyMatrix(4)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(3, 2)

graph.display()
