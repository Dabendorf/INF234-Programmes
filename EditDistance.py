import urllib.request
import sys
import numpy as np
import Levenshtein as ls

def alpha(letter1: str, letter2: str) -> int:
	"""# Advanced function
	vowals = ['a', 'e', 'i', 'o', 'u']
	con = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
	if letter1 == letter2:
		return 0
	elif letter1 in vowals and letter2 in vowals:
		return 1
	elif letter1 in con and letter2 in con:
		return 1
	else:
		return 3"""

	# Easy function
	if letter1 == letter2:
		return 0
	else:
		return 1

def min_dist(word1: str, word2: str) -> int:
	delta = 1
	len_word1 = len(word1)
	len_word2 = len(word2)

	A = [[None for x in range(len_word2+1)] for y in range(len_word1+1)]

	for i in range(len_word1+1):
		A[i][0] = i*delta
	for j in range(len_word2+1):
		A[0][j] = j*delta


	for j in range(1, len_word2+1):
		for i in range(1, len_word1+1):
			val1 = alpha(word1[i-1], word2[j-1]) + A[i-1][j-1]
			val2 = delta + A[i-1][j]
			val3 = delta + A[i][j-1]
			A[i][j] = min(val1, val2, val3)

	print("Horizontal: "+word1)
	print("Vertikal: "+word2)
	print(np.matrix(np.transpose(A)))
	return A[len_word1][len_word2]

# Programme for homework purpose and knuths list of words
def main():
	word1 = sys.argv[1]
	word2 = sys.argv[2]
	dist = min_dist(word1 = word1, word2 = word2)

	print("Word 1: "+word1)
	print("Word 2: "+word2)
	print("Minimum distance: "+str(dist))
	print("Levensthein Distance: "+str(ls.distance(word1, word2)))
	print(ls.editops(word1, word2))

if __name__ == "__main__":
	main()