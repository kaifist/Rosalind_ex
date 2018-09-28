# Enumerating k-mers Lexicographically

##import itertools as it
##
##with open('rosalind_lexf.txt') as file:
##	letras = file.readline().rstrip('\n').split()
##	letras2 = ''.join(letras)
##	print(letras2)
##	n = int(file.readline())
##
##	print(letras)
##	print(letras2)
##	lista_perm = it.product(letras2, repeat=n)
##
##	for i in lista_perm:
##		print(''.join(i))

# los ordena directamente en orden alfabetico

## Ordering Strings of Varying Length Lexicographically

# recursividad?

letras = ['D', 'N', 'A']

def lex(l, n, m = ''):
	print(m)
	if n == 1:
		for i in l:
			m += i
			return(m)
	else:
		for i in l:
			lex(l, m+i, n-1)

print(lex(letras, 1))

# letras = ('N', 'D', 'U', 'R', 'A', 'F', 'O', 'W', 'P', 'H')

# for i in letras:
# 	print(i)
# 	for j in letras:
# 		print(i+j)
# 		for h in letras:
# 			print(i+j+h)
# 			for l in letras:
# 				print(i+j+h+l)