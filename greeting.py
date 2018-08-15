import os

current = os.getcwd()
print(current)

home = os.path.expanduser('~')
print(home)

def greet(name):
	print('NAMASTE {}'.format(name))