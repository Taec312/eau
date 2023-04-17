import sys
"""
Entre min et max
Créez un programme qui affiche toutes les valeurs comprises entre deux nombres dans l’ordre croissant. Min inclus, max exclus.
"""
def between():
	l=""
	nb = begin
	while nb < last :
		l += str(nb) + " "
		nb += 1	
	print(l)

def main():							#defini quel est la plus petit valeur et rend les variable accessible a tous
	global begin
	global last
	if sys.argv[1] <= sys.argv[2]:
		begin= int(sys.argv[1])
		last = int(sys.argv[2])
	else:
		begin= int(sys.argv[2])
		last = int(sys.argv[1])
	between()

if __name__ == '__main__':
	main()