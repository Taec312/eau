import sys
"""
Majuscule sur deux
Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. Seule les lettres (A-Z, a-z) sont prises en compte.

crée 2 liste d'alaphabet regarder l'indice de la lettre et la remplacver avec le meme indice sur par la'autre liste
minuscule = ("a","b","c"...)
majuscule = ("A","B","C"...)
"""
def uppercase():
	global arg
	arg.lower()
	i = 0
	a = ""
	while len(arg) > i:
		a = arg[i].upper()
		arg = a
		i += 2
	print(arg)

if __name__ == '__main__':
	arg = sys.argv[1]
	uppercase()

#probleme on ne peut pas changer de str[i]= x ca ne marche pas