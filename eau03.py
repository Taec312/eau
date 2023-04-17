import sys
"""
Suite de Fibonacci
Créez un programme qui affiche le N-ème élément de la célèbre suite de Fibonacci. (0, 1, 1, 2) étant le début de la suite et le premier élément étant à l’index 0.
"""		
def n_element_fibonacci():
	list_Fibonacci = [0,1]									#pour avoir les 2 première valeur 												
	if n == 0:
		print("0")
	elif n == 1:
		print("1")
	else:
		for i in range(n-1):
			var = list_Fibonacci[i]+ list_Fibonacci[i+1]
			list_Fibonacci.append(var)
		print(list_Fibonacci[-1])

if __name__ == '__main__':
	n = int(sys.argv[1])
	n_element_fibonacci()