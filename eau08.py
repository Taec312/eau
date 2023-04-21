import sys
"""
Chiffres only
Créez un programme qui détermine si une chaîne de caractères ne contient que des chiffres.
"""

def juste_number():
	number = "123456789" 
	i = 0
	while i < len(arg):
		try:
			number.index(arg[i])
		except Exception as e:
			return False
		finally:
			i += 1
	return True

def main():
	if juste_number() == True:
		print("True")
	else:
		print("False")

if __name__ == '__main__':
	arg = sys.argv[1]
	main()

