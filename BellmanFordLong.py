import networkx as nx
import pprint as pp

# Calculates shortest path in graph
# Raises Negative cost cycle detected error if there is a negative cost cycle (obviously)

G = nx.DiGraph()
#e = [('a', 's', 12), ('s', 'c', 10), ('s', 'b', 11), ('b', 'a', 3), ('a', 'd', 5), ('d', 'b', -7), ('b', 'e', 20), ('c', 'b', 8), ('e', 'c', 9), ('c', 'f', 10), ('d', 'e', -20), ('d', 't', 19), ('e', 't', 9), ('f', 'e', -15), ('f', 'g', 11), ('g', 't', 12)]
#e = [('a', 's', 12), ('s', 'c', 10), ('s', 'b', 11), ('b', 'a', 3), ('a', 'd', 5), ('d', 'b', -7), ('b', 'e', 20), ('c', 'b', 8), ('e', 'c', 9), ('c', 'f', 10), ('d', 'e', -26), ('d', 't', 19), ('e', 't', 9), ('f', 'e', -15), ('f', 'g', 11), ('g', 't', 12)]
e = [('a', 'b', -4), ('c', 'b', 8), ('c', 't', 3), ('a', 't', -3), ('d', 'a', 6), ('d', 't', 4), ('e', 't', 2), ('e', 'c', -3), ('b', 'e', -2), ('b', 'd', -1),]
G.add_weighted_edges_from(e)

start = "t"
end = "t"

G = G.reverse()
dist = dict()
for v in G.nodes():
	dist[v] = float('inf')
dist[start] = 0
pre = dict()

for i in range(len(G.nodes)-1):
	print("New distances: "+str(dist))
	for u, v in G.edges():
		if dist[u] + G[u][v]["weight"] < dist[v]:
			dist[v] = dist[u] + G[u][v]["weight"]
			pre[v] = u

for u, v in G.edges():
	if dist[u] + G[u][v]["weight"] < dist[v]:
		print("Negative cycle!")

print(dist)
print(pre)