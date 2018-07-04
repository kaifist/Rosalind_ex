# find failure array with Knuth-Morris-Pratt algorithm

# read fasta file an get a complete adn string

# with open('rosalind_kmp.txt') as file:
# 	g = ''
# 	first = True
# 	for line in file:
# 		if line[0] == '>':
# 			if not first:
# 				#print(g)
# 				g = ''
# 			else:
# 				first = False
# 		else:
# 			g += line.strip()
# 	print(g)

s = 'CAGCATGGTATCACAGCAGAG'

fail_array = []
j = 0


for i in range(len(s)+1):
	fail_array.append(0)



for i in range(1,len(s)):
	if j == 0:
		sub_s = s[j:i]
		
		j+=1
	elif sub_s in s[0:i-j+2]:

		sub_s = s[j:i]
		#j = 


		fail_array.append(len(sub_s))

print(fail_array)




# import sys

# if __name__=="__main__":
#     g = ""
#     first = True
#     for line in sys.stdin:
#         if line[0] == ">":
#             if not first:
#                 print(g)
#                 g = ""
#             else:
#                 first = False
#         else:
#             g += line.strip()
#     print(g)

