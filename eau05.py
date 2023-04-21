import sys
"""
String dans string
Créez un programme qui détermine si une chaîne de caractère se trouve dans une autre.
"""
def inside_or_not():
	boolean = None
	try:
		first.index(second)
	except Exception as e:
		boolean = False
	else:
		boolean = True
	finally:
		print(boolean)
	
			

def main():
	global first
	global second
	
	if len(sys.argv) != 3:
		print("erreur")
	elif sys.argv[1] > sys.argv[2]:
		first = sys.argv[1]
		second = sys.argv[2]
	else:
		first = sys.argv[2]
		second = sys.argv[1]
	inside_or_not()

if __name__ == '__main__':
	main()