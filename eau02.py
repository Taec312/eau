import sys
"""
Paramètres à l’envers
Créez un programme qui affiche ses arguments reçus à l’envers.
"""		

def display_invese_param():
	taille = len(sys.argv)-1							
	x = taille
	for i in range(taille):
		print(sys.argv[x-i])

if __name__ == '__main__':
	display_invese_param()