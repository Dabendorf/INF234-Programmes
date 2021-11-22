import sys
import numpy as np

# Input: maximum weight w, sequence of weights, separated by S,
# sequence of values, separated by S
def main():
	W = int(sys.argv[1])
	weights_str = sys.argv[2].strip().split("S")

	weights = list(map(int, weights_str))

	values_str = sys.argv[3].strip().split("S")
	values = list(map(int, values_str))

	print("W: "+str(W))
	print("Weights: "+str(weights))
	print("Values: "+str(values))

	# Memory of size (n+1)*(W+1)
	n = len(weights)
	M = [[None for x in range(W+1)] for y in range(n+1)]

	for w in range(W+1):
		M[0][w] = 0
	print("Memory init:")
	print(np.matrix(M))

	# Looping through every index N
	# and in inner loop through all possible weights
	for i in range(1,n+1):
		print("Round: "+str(i))
		for w in range(0,W+1):
			if w < weights[i-1]:
				M[i][w] = M[i-1][w]
			else:
				M[i][w] = max(M[i-1][w], M[i-1][w-weights[i-1]] + values[i-1])
		print(np.matrix(M))

	print("Maximum value: "+str(M[n][W]))
	# Get items

	subsum = 0
	n_ind = n
	W_ind = W
	el_list = []
	val_list = []

	while subsum < M[n][W]:
		n_ind -= 1
		path1 = M[n_ind][W_ind]
		path2 = M[n_ind][W_ind-weights[n_ind]]
		
		if path2+values[n_ind] == M[n_ind+1][W_ind]:
			# print("Path left")
			# Path 2 correct (left), element added
			el_list.append(weights[n_ind])
			val_list.append(values[n_ind])
			subsum += (values[n_ind])
			W_ind -= weights[n_ind]
		"""else:
			print("Path right")
			# Path 1 correct (right), no element added"""

	print("Choosen elements: ")
	print(el_list)
	print("Values: ")
	print(val_list)

	
	

if __name__ == "__main__":
	main()