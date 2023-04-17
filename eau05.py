import sys
"""
String dans string
Créez un programme qui détermine si une chaîne de caractère se trouve dans une autre.
"""
def inside_or_not():
	if len(first) >= len(second):
		for i in range(len(first) ):
			if first[0] == second[0]:
				for i in range(len(second) ):
					if first[i] != second[i]:
						break
					else:
						print("")
					print("vrai")
				return 1
		print("faux")
	else:
		for i in range(len(second) ):
			if first[0] == second[0]:
				for i in range(len(first) ):
					if first[i] != second[i]:
						break
					else:
						print("")
					print("vrai")
				return 1
		print("faux")
	"""des que la premier lettre est commun on regarde la suite avec une boucle sinon 
			on regarde lettre par lettre jusqu'a la fin pour verifier qu'il n'y a pas une nouvelle lette """
			

def main():
	if len(sys.argv) != 3:
		print("erreur")
	else:
		inside_or_not()

if __name__ == '__main__':
	first = sys.argv[1]
	second = sys.argv[2]
	main()