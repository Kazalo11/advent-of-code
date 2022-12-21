from collections import defaultdict
import networkx as nx


class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, u, v, weight):
        self.edges[u].append(v)
        self.weights[(u, v)] = weight


graph = Graph()
grid = []
grid_value = []
with open('day12input.txt') as f:
    for line in f:
        line = line.strip()
        line = list(line)
        grid.append(line)
        grid_value.append([0] * len(line))

G = nx.Graph()
values = []
count = 1
a_values = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        test = grid[i][j]
        if test == 'S':
            test = 'a'
        elif test == 'E':
            test = 'z'
        grid_value[i][j] = ord(test)

        if grid[i][j] in values:
            grid[i][j] = grid[i][j] + str(count)
            count += 1
        values.append(grid[i][j])
        if grid[i][j][0] == 'a':
            a_values.append(grid[i][j])

for i in range(len(grid)):
    for j in range(len(grid[0])):
        current = grid_value[i][j]
        if i != 0:
            check = grid_value[i - 1][j]
            if (check - current) <= 1:
                graph.add_edge(grid[i][j], grid[i - 1][j], 1)
                G.add_edge(grid[i][j], grid[i - 1][j])
        if i != len(grid) - 1:
            check = grid_value[i + 1][j]
            if (check - current) <= 1:
                graph.add_edge(grid[i][j], grid[i + 1][j], 1)
                G.add_edge(grid[i][j], grid[i + 1][j])
        if j != 0:
            check = grid_value[i][j - 1]
            if (check - current) <= 1:
                graph.add_edge(grid[i][j], grid[i][j - 1], 1)
                G.add_edge(grid[i][j], grid[i][j - 1])
        if j != len(grid[0]) - 1:
            check = grid_value[i][j + 1]
            if (check - current) <= 1:
                graph.add_edge(grid[i][j], grid[i][j + 1], 1)
                G.add_edge(grid[i][j], grid[i][j + 1])


def dijsktra(graph, initial, end):
    shortest = {initial: (None, 0)}
    current = initial
    visited = set()

    while current != end:
        visited.add(current)
        dest = graph.edges[current]
        current_weight = shortest[current][1]

        for next_node in dest:
            weight = graph.weights[(current, next_node)] + current_weight
            if next_node not in shortest:
                shortest[next_node] = (current, weight)
            else:
                current_shortest = shortest[next_node][1]
                if current_shortest > weight:
                    shortest[next_node] = (current, weight)
        next_dest = {node: shortest[node] for node in shortest if node not in visited}
        if not next_dest:
            return float('inf')
        current = min(next_dest, key=lambda k: next_dest[k][1])

    path = []
    while current is not None:
        path.append(current)
        next_node = shortest[current][0]
        current = next_node
    path = path[::-1]
    return len(path)


answer = 10000
for item in a_values:
    answer = min(len(nx.shortest_path(G,item,'E')), answer)
    print(answer)
