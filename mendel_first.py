# Rosalind Ex Mendel's First Law

import random
import numpy as np
def mendel_1st(x, y):

	total = x + y
	bag = ['x', 'y']

	choice = random.choice(bag)

	if choice == 'x':
		pass

k_n = (2/4 * 1/3) + (2/4 * 2/3) + (2/4*2/3) 


k_m = (2/4 * 1/3) + (2/4*2/3) + (2/4*2/3) + (2/4*1/3)

m_n = (2/4*1/3) + (2/4*2/3) + (2/4*2/3)

print(k_n * k_m * m_n)

print(0.333+0.333+0.250+0.5)

### simulates n trials (no es mi solucion) 
import random
k = 2
m = 2
n = 2

trials = 0
dominants = 0

while trials < 1:
    s = ['AA'] * k + ['Aa'] * m + ['aa'] * n
    first = random.choice(s)
    s.remove(first)
    second = random.choice(s)
    has_dominant_allele = 'A' in [random.choice(first), random.choice(second)]
    trials += 1
    if has_dominant_allele:
        dominants += 1
    print ("%.5f" % (dominants / float(trials)))

### calculates prob given k, m and n (not my solution too)

from itertools import product

k = 30  # AA  homozygous dominant
m = 20  # Aa  heterozygous
n = 29  # aa  homozygous recessive

population = (['AA'] * k) + (['Aa'] * m) + (['aa'] * n)

all_children = []
for parent1 in population:
    # remove selected parent from population.
    chosen = population[:]
    chosen.remove(parent1)
    for parent2 in chosen:
        # get all possible children from 2 parents. Punnet square
        children = product(parent1, parent2)
        all_children.extend([''.join(c) for c in children])

#dominants = filter(lambda c: 'A' in c, all_children)

dominants = []
for dominant in all_children:
	if 'A' in dominant:
		dominants.append(dominant)
# float for python2
print (float(len(list(dominants))) / len(all_children))
