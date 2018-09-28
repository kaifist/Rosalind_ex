#import max_gc_content as GC
from math import log10
import re

def log_prob(s, x):
	P = 1.0 	# as does not affect by multiplication (instead of 0.0)
	for base in s:
		if base == 'A' or base == 'T':
			P *= (1-x)/2
		if base == 'G' or base == 'C':
			P *= x/2

	return log10(P)

def log_prob2(s, x):
	P = log10(1.0) 	# as does not affect by multiplication (instead of 0.0)
	for base in s:
		if base == 'A' or base == 'T':
			P += log10((1-x)/2)
		if base == 'G' or base == 'C':
			P += log10(x/2)

	return (P)

with open('rosalind_prob.txt') as file:
	adn = file.readline().rstrip('\n')
	arr_line = file.readline().rstrip('\n').split(' ')
	A_array = [float(num) for num in arr_line]
	print(A_array)

	B_array = []
	for i in A_array:
		B_array.append(log_prob2(adn, i))


print(B_array)
		


		


