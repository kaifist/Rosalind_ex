#fibonacci again

uno = 1 
dos = 1
print(uno)
print(dos)
n = 2
real = 2016 
while True:

	tres = uno + dos
	n += 1
	print (tres)
	if n == real:
		break

	uno = tres + dos
	n += 1
	print (uno)
	if n == real:
		break
	
	dos = uno + tres
	n += 1
	print (dos)
	if n == real:
		break
	