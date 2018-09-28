# get gc contnet forma fasta file and return the highest


with open('rosalind_gc.txt') as file:
	fasta_dict = {}
	
	for i in file:
		line = i.rstrip('\n')
		
		if i[0] == '>':
			fasta_ind = line
			adn = ''         # empty the string adn each time > is found

		else:				 # join all dna lines in one string
			adn += i.rstrip('\n')

		fasta_dict[fasta_ind] = adn 

print(fasta_dict)
def count_GC(dicc):
	list_porc = []	
	for key in dicc:
		G = dicc[key].count('G')
		C = dicc[key].count('C')
		porc = ((G+C)/len(dicc[key]))*100
		list_porc.append((porc, key[1:]))
	
	return list_porc

print(max(count_GC(fasta_dict))[::-1])



