import os
from os import path

current = os.getcwd()
print(current)

parent = os.path.dirname(current)

home = os.path.expanduser('~')
print(home)

def greet(name):
	print('NAMASTE {}'.format(name))