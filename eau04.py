import sys	
"""
Prochain nombre premier
Créez un programme qui affiche le premier nombre premier supérieur au nombre donné en argument.
"""
def prime_number():
	if nb == 0 or nb == 1:
		return 0
	else:
		i = 2																	
		while i != nb:
			if nb % i == 0 and i != nb: 
				
				return 0															
			else:
				i+= 1
	return 1


def first_prime_number():
	global nb
	while prime_number() != True:
		nb +=1
	print(nb)
if __name__ == '__main__':
	nb = int(sys.argv[1])
	first_prime_number()