# A C G T

def count_base(s, b):
	print(s.count(b))

# ex 1
s = 'ACGTACGATGCAGATCGACTACG'
base_list = ['A', 'C', 'G', 'T']

for i in base_list:
	count_base(s, i)


with open('rosalind_dna.txt') as file:
	base_list = ['A', 'C', 'G', 'T']
	dna_s = file.readline()
	for i in base_list:
		count_base(dna_s,i)
	


# ex2

with open('rosalind_rna.txt') as file:
	adn = file.readline()
	rna = adn.replace('T', 'U')
	print rna

sample = 'ACGTACGATGCAGATCGACTACG'
rna = sample.replace('T', 'U')
print rna

# ex3 complementary

comp_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
sample = 'ACGTACGATGCAGATCGACTACG'

def compl(s):
	comp = ''
	for i in s:
		comp += comp_dict[i]
	com_rev = comp[::-1]
	print com_rev

with open('rosalind_revc.txt') as file:
	dna = file.readline().rstrip('\n')
	print 'solucion'
	compl(dna)


