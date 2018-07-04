# Hamming distance between s and t strings

with open('rosalind_hamm.txt') as file:
	s = file.readline().rstrip('\n')
	t = file.readline().rstrip('\n')


hamming = 0
#s = 'GAGCCTACTAACGGGAT'
#t = 'CATCGTAATGACGGCCT'
for i in range(len(s)):
	if s[i] != t[i]:
		hamming += 1

print(hamming)

# Ex permutaciones

import itertools

with open('rosalind_perm.txt') as file:
	n = int(file.readline())

	lista = list(range(1,n+1))

	n_perm = 0
	l_perm = itertools.permutations(lista, n)

	for i in l_perm:
		n_perm +=1
		print(' '.join(map(str, i)))
		


print(n_perm)