class Graph():
    def __init__(self,size):
        self.matrix = []
        for i in range(size):
            self.matrix.append([float('inf') for i in range(size)])
        self.size = size

    def add_edge(self,v1,v2):
        self.matrix[v1][v2]