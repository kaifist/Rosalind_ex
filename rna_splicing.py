import ARNtoPROT_translate as aptrans
#import re



with open('rosalind_splc.txt') as file:

	adn = ''
	introns = []

	second = False  # condition to fill the introns list
	file.readline() # escape the first line
	
	for line in file:
		if line[0] == '>': # first time > appears introns begin
			second = True  

		else:
			if second: 
				introns.append(line.strip())
			if not second:
				adn += line.strip()
		


def splicing(dna, introns):
	'''remove each intron'''
	for intron in introns:
		pre_rna = dna.replace(intron, '')
		dna = pre_rna

	return pre_rna


def dnatorna(rnap):
	rnam = rnap.replace('T', 'U')
	return rnam



rnap = splicing(adn, introns)

rnam = dnatorna(rnap)

# translate the rnam into protein
prot = aptrans.trarntoprotion(rnam)

print(prot)


