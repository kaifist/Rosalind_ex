import re

adn = 'GATATATGCATATACTT'
pattern = r'(ATAT)'

match = re.search(pattern, adn)
print(re.findall(pattern, adn)) #overlapped=True))
print(match.group())


runs = re.finditer(pattern, adn)
for i in runs:
	i_start = i.start()
	print(i_start+1)

print('-'*15)

def motifs(pattern, adn):
	for match in range(0,len(adn)-len(pattern)):
		target = adn[match:match+len(pattern)]
		if target == pattern:
			print(match+1)

adn = 'GGATCTAGCTCACGGACTCACGGTGCTCACGGCTCACGGCTCACGGTACCACTCACGGGCTCACGGCTCACGGGACTCACGGACTCACGGCTCACGGCGCTCACGGGTAGCGCTCACGGGACTCACGGCTCACGGCTCACGGCACGTCCTCACGGCAATTCCAACTCACGGCCAAACTCACGGTGCGTTCTCACGGGAACGTCCGCTGCTCACGGCGCTCACGGAGGCTCACGGGCTCACGGGTGTCCTCACGGCTCACGGTATCAACTGCTCACGGCTCACGGATCCTCACGGCCAGGCCTCACGGGGAACGCTCACGGTTTGCTCACGGTCTCCTCACGGAACCTCATCTCACGGATCCTCACGGAACTCACGGGCTCACGGAAACTCACGGTGCTCACGGACGCTCACGGTCCTCACGGCTCACGGCCTCACGGGGGACTCACGGGCTCACGGTCTGGAGCCTCACGGCTCACGGTCTCACGGTAATCTCACGGATCCTCACGGCCTCACGGCAAGCTCACGGCTCACGGCTCACGGCCCCTCACGGGCTCACGGCTCACGGTCTCACGGACTCACGGGACACGCCACTCTCACGGTAAGTTTATTGCTCACGGCTCACGGTCTCACGGCTCACGGAGGACTCACGGGCCTCACGGTAGTACCTCACGGAATCTCACGGTGTCTTACTCACGGCTCACGGGTTTGGTATCTCACGGATCGAAAGCTCACGGTGTCCTCACGGCACTCACGGCCGGTTTTCAATGCTCACGGATGGGCCATACTCACGGTCCTCACGGGACTCACGGAGCGGAGCGCTCACGGAGGGCTCACGGAATGCTCACGGTATTTCCCCTCCTCACGGCTCACGGCTCACGGTCTCACGGCTCACGGTACGCTCACGGAGCTCACGGCATTACCGCTCACGGATTGCAACTCACGGCTCACGGGATCTCACGGGCTCACGGATGCTCACGG'
pattern = 'CTCACGGCT'

motifs(pattern, adn)
print('-'*15)

def motif_location(motif, dna):
    results = []
    position = 0
    pattern = re.compile(motif)
    print(pattern)

    while True:
        r = pattern.search(dna, position)
        if not r:
            break
        position = r.start() + 1
        results.append(str(position))
    return ' '.join(results)



print(motif_location(pattern, adn))


