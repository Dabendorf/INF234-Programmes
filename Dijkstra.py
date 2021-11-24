import sys
import numpy as np
from networkx.exception import NetworkXError, NetworkXNoPath
import networkx as nx
import pprint as pp
import queue

# python Dijkstra.py start_node
# Python Dijkstra.py s
def main():
	start_node = sys.argv[1]
	edge_weights = [('0', '1', 5),
					('0', '2', 5),
					('1', '2', 8),
					('0', '4', 9),
					('2', '4', 7),
					('0', '3', 6),
					('1', '5', 8),
					('2', '5', 3),
					('1', '6', 4),
					('6', '7', 9),
					('3', '5', 9),
	]

	G = nx.Graph()
	G.add_weighted_edges_from(edge_weights)

	pp.pprint(list(G.edges(data=True)))
	dijkstra(G, start_node)


def dijkstra(G: nx.DiGraph, s):
	q = queue.PriorityQueue()
	num_of_nodes = G.number_of_nodes()
	print("num of nodes: "+str(num_of_nodes))
	
	dist = dict()
	pre = dict()
	for i in G.nodes():
		dist[i] = float('inf')
	for i in G.neighbors(s):
		q.put((G[s][i]["weight"],i))
	dist[s] = 0
	q.put((0, s))

	visited = []

	while not q.empty():
		u = q.get()[1]

		if u not in visited:
			print("========")
			print("Next node: "+str(u))
			for v in G.neighbors(u):
				if v not in visited:
					print("Neighbour: "+str(v))
					alt = dist[u] + G[u][v]['weight']
					print("Alternative distance: "+str(alt))
					print("Old distance: "+str(dist[v]))
					if alt < dist[v]:
						dist[v] = alt
						q.put((alt, v))
						pre[v] = u

			print("Distances: ")
			print(dist)

			visited.append(u)

	print("Visited:")
	print(visited)
	print("Predecessor:")
	print(pre)
	print("Distances: ")
	print(dist)

	
	

if __name__ == "__main__":
	main()