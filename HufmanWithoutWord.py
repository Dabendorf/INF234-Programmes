import sys
from networkx.exception import NetworkXError, NetworkXNoPath
import numpy as np
import networkx as nx
from collections import defaultdict
import pprint, json

# Calculates the huffman tree, but does not generate code, since no serious left right relation exists
def main():
	"""input_str = sys.argv[1]
	print("Input: "+input_str)

	counter = defaultdict(int)
	for letter in str(input_str):
		if letter != "_":
			counter[letter] += 1"""
	# Insert frequencies
	counter = {"A": 60, "B": 15, "C": 42, "D": 10, "E": 50, "F": 56, "G":12}
	# counter = {"A": 14, "B": 7, "C": 9, "D": 18, "E": 19}

	ancestors = dict()

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
		
		ancestors[overall_str] = (min_letter1, min_letter2)
		counter[overall_str] = min_letter_val1+min_letter_val2

		root = overall_str
	print("Root: "+root)
	print("Ancestors: "+str(ancestors))

	fs = dict()
	fs[root] = ""
	binary_strings_temp = calc_binary_strings(ancestors=ancestors, root=root, final_strings=fs)
	print("Binary strings: "+str(binary_strings_temp))
	
	binary_strings = dict()
	for k, v in binary_strings_temp.items():
		if len(k) == 1:
			binary_strings[k] = v
	print("Binary strings: "+str(binary_strings))

	"""final_hufman_str = ""
	for letter in str(input_str):
		if letter != "_":
			final_hufman_str += binary_strings[letter] + "|"
		else:
			final_hufman_str += " "

	print("Hufman string for "+input_str)
	print(final_hufman_str)"""

def calc_binary_strings(ancestors: dict, root: str, final_strings: dict) -> dict:
	if root not in ancestors:
		return final_strings
	else:
		left_str, right_str = ancestors[root]
		final_strings[left_str] = final_strings[root] + "0"
		final_strings[right_str] = final_strings[root] + "1"
		fs1 = calc_binary_strings(ancestors=ancestors, root=left_str, final_strings=final_strings)
		fs2 = calc_binary_strings(ancestors=ancestors, root=right_str, final_strings=final_strings)
		z = {**fs1, **fs2}
		return {**final_strings, **z}

if __name__ == "__main__":
	main()