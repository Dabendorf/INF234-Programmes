import sys
from networkx.exception import NetworkXError, NetworkXNoPath
import numpy as np
import networkx as nx
from collections import defaultdict
import pprint, json

# Calculates the huffman tree, but does not generate code, since no serious left right relation exists
def main():
	input_str = sys.argv[1]
	print("Input: "+input_str)

	counter = defaultdict(int)
	for letter in str(input_str):
		if letter != "_":
			counter[letter] += 1

	T = nx.Tree

	while len(counter) > 1:
		print("=========\nNew iteration")
		print("Counter: ")
		print(json.dumps(counter, indent=4))
		# Find minimum letters and delete them from dict
		min_letter1 = min(counter, key=counter.get)
		min_letter_val1 = counter[min_letter1]
		counter.pop(min_letter1)

		min_letter2 = min(counter, key=counter.get)
		min_letter_val2 = counter[min_letter2]
		counter.pop(min_letter2)

		overall_str = min_letter1+min_letter2
		print("Draw branches: root: "+overall_str+", left (0): "+min_letter1+", right (1): "+min_letter2)
		
		counter[overall_str] = min_letter_val1+min_letter_val2

if __name__ == "__main__":
	main()