import sys
"""
Index wanted
Créez un programme qui affiche le premier index d’un élément recherché dans un tableau. Le tableau est constitué de tous les arguments sauf le dernier. L’élément recherché est le dernier argument. Afficher -1 si l’élément n’est pas trouvé.
"""

def research_word():
	i = 0
	while i < len(arg)-1 :
		if arg[i] == word:
			return i
			print(ka)
		else:
			i +=1
			print(arg[i])
	return -1

def main():
	print(research_word() )
	a = sentence = arg.split(" ")
	print(a)

if __name__ == '__main__':
	arg = sys.argv[1]
	word = sys.argv[2]
	main()

#transformer un tableau et apris recherche for avec return 