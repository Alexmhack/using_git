from pathlib import Path

current = Path.cwd()
print(current)


def greet(name):
	print('NAMASTE {}'.format(name))