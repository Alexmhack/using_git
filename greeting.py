from pathlib import Path

home = Path.cwd()
print(home)

def greet(name):
	print('NAMASTE {}'.format(name))