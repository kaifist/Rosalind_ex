# Averages. Expected value of X (Esperanza matemática) in URV
# uniform random variable

# Given six integers (+) number of couples in a pop with each 
# genotype pairing for a given factor (Mendelian unit of heredity)
# 

# this order AA-AA (100) AA-Aa (100) AA-aa (100) Aa-Aa (75) Aa-aa (50) aa-aa (0)

# expected dominant offspring

#with open('') as file:
#	pass

Prob_off = [1.0, 1.0, 1.0, 0.75, 0.5, 0]



def exp_off(l):
	expected_off = 0 
	# assuming two offspring per couple
	l2 = [ 2*i for i in l]
	# sumeach(offspring x prob)
	for i in range(len(l2)):
		expected_off += l2[i]*Prob_off[i]  
	print(expected_off)

l = [16948, 16400, 19196, 16870, 19233, 17319]

exp_off(l)


