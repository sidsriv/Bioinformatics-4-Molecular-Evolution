import sys
from collections import defaultdict, deque

filename = sys.argv[1]

with open(filename) as file:
	data = []
	for line in file:
		data.append(line[:-1])

n = int(data[0])

from_node = []
to_node = []
weight = []

for line in data[1:]:
	x = line.split('->')
	from_node.append(int(x[0]))
	x = x[1].split(':')
	to_node.append(int(x[0]))
	weight.append(int(x[1]))

#print from_node,to_node,weight

nodes = list(set(from_node))

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    
    if origin == destination:
    	return 0
    else:
    	visited, paths = dijkstra(graph, origin)
    	full_path = deque()
    	_destination = paths[destination]

    	while _destination != origin:
        	full_path.appendleft(_destination)
        	_destination = paths[_destination]

    	full_path.appendleft(origin)
    	full_path.append(destination)

    	return visited[destination]#, list(full_path)


graph = Graph()

for node in nodes:
	graph.add_node(node)

for i in range(len(from_node)):
	graph.add_edge(from_node[i],to_node[i],weight[i])

leaf_nodes = []
for i in graph.edges:
	if len(graph.edges[i])==2:
		leaf_nodes.append(i)

for i in leaf_nodes:
	for j in leaf_nodes:
		print str(shortest_path(graph,i,j))+ ' ', 
	print '\n'