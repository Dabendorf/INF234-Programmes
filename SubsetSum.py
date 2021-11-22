import sys
import numpy as np

# Input: maximum weight w, sequence of weights, separated by S
# python SubsetSum.py 20 3S4S5S7S11
def main():
	W = int(sys.argv[1])
	weights_str = sys.argv[2].strip().split("S")

	weights = list(map(int, weights_str))

	print("W: "+str(W))
	print("Weights: "+str(weights))

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
				M[i][w] = max(M[i-1][w], M[i-1][w-weights[i-1]] + weights[i-1])
		print(np.matrix(M))

	print("Maximum subsetsum: "+str(M[n][W]))
	# Get items

	subsum = 0
	n_ind = n
	W_ind = W
	el_list = []
	while subsum < M[n][W]:
		n_ind -= 1
		path1 = M[n_ind][W_ind]
		path2 = M[n_ind][W_ind-weights[n_ind]]
		
		if path1+weights[n_ind] == M[n_ind+1][W_ind]:
			print("Path right")
			# Path 1 correct (right), no element added
		else:
			print("Path left")
			# Path 2 correct (left), element added
			el_list.append(weights[n_ind])
			subsum += (weights[n_ind])
			W_ind -= weights[n_ind]

	print("This is wrong (I don't know why)")
	print(el_list)

	
	

if __name__ == "__main__":
	main()