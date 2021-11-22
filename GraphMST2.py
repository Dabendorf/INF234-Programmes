import sys
from networkx.exception import NetworkXError, NetworkXNoPath
import numpy as np
import networkx as nx
import pprint

G = nx.Graph()

edge_weights = [('A', 'B', 19),
				('A', 'C', 1),
				('A', 'D', 7),
				('A', 'E', 9),
				('A', 'F', 12),
				('A', 'G', 5),
				('B', 'G', 4),
				('B', 'H', 16),
				('C', 'H', 10),
				('I', 'H', 6),
				('C', 'I', 20),
				('D', 'I', 15),
				('J', 'I', 2),
				('L', 'G', 8),
				('L', 'F', 13),
				('F', 'K', 17),
				('E', 'K', 18),
				('E', 'J', 3),
				('K', 'J', 11),
				('K', 'L', 14)]

G.add_weighted_edges_from(edge_weights)


T_k = nx.minimum_spanning_tree(G, algorithm='kruskal')
T_p = nx.minimum_spanning_tree(G, algorithm='prim')


pp = pprint.PrettyPrinter(depth=4)
print("Sum of weights: "+str(T_k.size(weight="weight")))
pp.pprint(sorted(T_k.edges(data=True)))
print("Sum of weights: "+str(T_p.size(weight="weight")))
pp.pprint(sorted(T_p.edges(data=True)))