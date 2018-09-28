# get gc contnet forma fasta file and return the highest


with open('rosalind_gc.txt') as file:
	fasta_dict = {}

	while True:
		line = file.readline().rstrip('\n')

		try:
			if line[0] == '>':
		 		keys = [line]
		 		print(keys)
		 		continue
		except: break

	
	for i in file:
		line = i.rstrip('\n')
		if i[0] == '>':
			fasta_dict[line] = ''
			adn = ''
			#while 
			adn += file.readline().rstrip('\n')
			fasta_dict[line] = adn
			

print(fasta_dict)

def count_GC(dicc):
	list_porc = []	
	for key in dicc:
		G = dicc[key].count('G')
		C = dicc[key].count('C')
		porc = ((G+C)/len(dicc[key]))*100
		list_porc.append((key[1:],porc))
	
	return list_porc

#print(sorted(count_GC(fasta_dict)))




