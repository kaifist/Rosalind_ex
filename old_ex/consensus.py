import numpy as np

posibles = {
	'A': [],
	'C': [],
	'G': [],
	'T': []
			}

#with open('rosalind_cons.txt') as file:
with open('consensus_test.txt') as file:
	
		
	list_dna = []
	adn = None	
	for i in file:		         # empty the string adn each time > is found
		if i[0] == '>':
			if adn != None:
				list_dna.append(adn)				 # join all dna lines in one string
				adn = ''

		elif i[0] != '>':
			if adn == None:
				adn = i.rstrip('\n')
			else:
				adn += i.rstrip('\n')

	#print(list_dna)
	#list_dna = [line.rstrip('\n') for line in file  if line[0] != '>']
	zeroes = len(list_dna[0]) # because the len() of dna is always the same

# fill with zeroes the lists of the dictionary
	for key in posibles:
		for zero in range(zeroes):
			posibles[key].append(0)

# add 1 when find a base in the position i
	for dna in list_dna:	
		for i in range(len(dna)):
			#print(posibles)
			posibles[dna[i]][i] += 1 
	#print(posibles)
# get the consensus string
	consensus = ''

# first get a dict of lists with position and number of bases
	position = {}
	str_long = len(posibles['A'])

	n = 0
	while n < str_long:
		position[n] = []
		for base in posibles.keys():
			position[n].append(posibles[base][n])
		n+=1


	for i in position.keys():
		for base in posibles.keys():
			if max(position[i]) == posibles[base][i] and len(consensus) == i:

				
				consensus += base
	print(consensus, len(consensus))

	bases = ['A', 'C', 'G', 'T']
	for base in bases:

		print(base+':', ' '.join(map(str, posibles[base])))		








