# Programmes useful for INF234 course at UiB
This repository includes a lot of algorithms being useful for the UiB course [``INF234 Algorithms``](https://www.uib.no/en/course/INF234)

# Programmes
* ``BellmanFord.py``: Solving a distance problem with Bellman-Ford
* ``BellmanFordLong.py``: Solving a distance problem with Bellman-Ford printing states
* ``DFStime.py``: DFS including prefix order
* ``Dijkstra.py``: Solving a distance problem with Dijkstra
* ``EditDistance.py``: Calculating the EditDistance between two words
* ``FordFulkerson.py``: Finding the flow with FordFulkerson
* ``FordFulkersonInner.py``: Finding the flow with FordFulkerson by starting at one inner state
* ``GraphMST.py``: Solving Minimum Spanning Tree with Kruskal
* ``GraphMST2.py``: Solving Minimum Spanning Tree using networkx
* ``Hufman.py``: Calculates Hufman code
* ``HufmanWithoutWord.py``: Calculates Hufman Tree without generating the code
* ``Knapsack.py``: Solving a Knapsack problem
* ``ShortestDistance.py``: Calculates the EditDistance between two strings
* ``SubsetSum.py``: Solving a SubSet sum problem (special case of Knapsack)

# How to use them
## Subset sum
``python SubsetSum.py 20 3S4S5S7S11``<br>
Parameter: max weight, sequence of weights (separator: S)<br>
Attention: List of elements doesn't work, use Knapsack

## Knapsack
``python Knapsack.py 20 3S4S5S7S11 3S4S5S7S11``<br>
``python Knapsack.py 10 4S4S5S3S2S6 10S11S14S6S5S14``<br>
Parameter: max weight, sequence of weights (separator: S), sequence of values (S)<br>
Subset sum by setting weights and values equal

## Minimum Spannung tree
Two programmes: GraphMST self programmed Kruskal<br>
GraphMST2 is framework implementation of Prim and Kruskal<br>
GraphMST only accepts numbers as node names<br>
``python GraphMST.py``<br>
``python GraphMST2.py``

## Edit distance
Takes as input two words<br>
Calculates control value via Levensthein framework<br>
``python EditDistance.py klinger klingre``

## BellmanFord
Calculates shortest path in graph<br>
Input path lengths in code<br>
Does not output internal table<br>
Long version has output<br>
``python BellmanFord.py``<br>
``python BellmanFordLong.py``

## Dijkstra
Shortest path without negative edges<br>
Input path lengths in code<br>
Argument is start node<br>
``python Dijkstra.py a``

## FordFulkerson
Two programmes, one for the entire algorithm and one for one iteration<br>
<br>
Entire programme: insert edge weights in tuple orig_cap<br>
``python FordFulkerson.py``<br>
<br>
Just one iteration, three lists (third redundant, sorry)<br>
* orig_cap: edge weights in original graph<br>
* g_edges_used: used flow at the moment<br>
* g_f_edges: all edges of residual graph<br>
``python FordFulkersonInner.py``

## Hufman
insert string as argument, spaces with "_" string
Make sure the | are positioned like Pål wants them to be (like at beginning or end of word)<br>
Second programme without words, but frequencies<br>
``python HufmannTree.py testiest_sensitiveness``<br>
``python HufmanWithoutWord.py``
