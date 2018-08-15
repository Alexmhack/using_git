import os

current = os.getcwd()
print(current)

parent = os.path.dirname(current)
programs = os.path.join(parent, 'python_programs')

home = os.path.expanduser('~')
print(home)

def greet(name):
	print('NAMASTE {}'.format(name))