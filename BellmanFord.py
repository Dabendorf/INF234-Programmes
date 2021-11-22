import networkx as nx
import pprint as pp

# Calculates shortest path in graph
# Raises Negative cost cycle detected error if there is a negative cost cycle (obviously)

G = nx.DiGraph()
e = [('a', 's', 12), ('s', 'c', 10), ('s', 'b', 11), ('b', 'a', 3), ('a', 'd', 5), ('d', 'b', -7), ('b', 'e', 20), ('c', 'b', 8), ('e', 'c', 9), ('c', 'f', 10), ('d', 'e', -20), ('d', 't', 19), ('e', 't', 9), ('f', 'e', -15), ('f', 'g', 11), ('g', 't', 12)]
#e = [('a', 's', 12), ('s', 'c', 10), ('s', 'b', 11), ('b', 'a', 3), ('a', 'd', 5), ('d', 'b', -7), ('b', 'e', 20), ('c', 'b', 8), ('e', 'c', 9), ('c', 'f', 10), ('d', 'e', -26), ('d', 't', 19), ('e', 't', 9), ('f', 'e', -15), ('f', 'g', 11), ('g', 't', 12)]
G.add_weighted_edges_from(e)

start = "s"
end = "t"

print("Shortest path distance from s to every node and direct predecessor:")
pp.pprint(nx.bellman_ford_predecessor_and_distance(G, start, end))

print("Shortest path from "+start+" to "+end+":")
print(nx.bellman_ford_path(G, start, end))
print("Path length: ", end="")
print(nx.bellman_ford_path_length(G, start, end))

print("Paths to every node: ")
pp.pprint(nx.single_source_bellman_ford_path(G, start))