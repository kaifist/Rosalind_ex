def rabbit_pop(n, k):
	pop = 1 

	if n == 1:
		pop = 1

	elif n == 2:
		pop = 1
		
	else:
		pop = rabbit_pop(n-1, k) + rabbit_pop(n-2, k)*k
		#print (pop)
	return pop

		


def rab1(n, k): # faster than rabbit_pop
	ad = 0
	kit = 1
	for month in range(n):
		ad, kit = ad + kit, ad * k

	return ad 

# mortality
def rab2(n, k, m):
	ad = 0
	kit = 1
	death = 1
	for month in range(1,n+1):
		if month <= m:
			ad, kit = ad + kit, ad * k
		if month > m:
			ad -= death
			ad, kit =  ad + kit, ad
	return ad

def rab3(n, k, m):
	kit = 1
	ad = 0
	pre = 0
	for month in range(2,n+1):
		# pop total = adults + kittens 
		# por cada kit habrá 
		if month == 2:
			pre += kit
			kit -= pre
			
		if month == 3:
			ad = pre
			pre -= ad
			kit += k
		if month == 3:
			pass

			
		elif month > m:
			pass
			
			
	print('adults', ad)
	print('kittens', kit)
	print('pread', pre)
	if n <= m: return ad+kit+pre
	#else: return pop


#print rabbit_pop(33, 2)
#print(rab1(33,1))


def rab1_dead(n, m): 
	ad = 0
	kit = 1
	death = 0
	for month in range(n):
		kit += 1
		ad += 1


	for month in range(1,n+1,m):
		death += 1
		ad -= death

	return ad+kit-ad
		

#print (rab2(6,1,3))

#print (rab2(92,1,17))
print ('1: ',rab3(1,1,3))
print ('2: ',rab3(2,1,3))
print ('3: ',rab3(3,1,3))
print ('4: ',rab3(4,1,3))
print ('5: ',rab3(5,1,3))
print ('6: ',rab3(6,1,3))
print ('7: ',rab3(7,1,3))
print ('8: ',rab3(8,1,3))
print ('9: ',rab3(9,1,3))
