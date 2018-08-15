from pathlib import Path

current = Path.cwd()
print(current)

home = Path.home()
print(home)


def greet(name):
	print('NAMASTE {}'.format(name))