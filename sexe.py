#!/usr/bin/env python2

import sys

data = []
values = []

def digest():
	global data
	pass

def compute(prenom):
	return False

def toVector(prenom):
	res = [0] * 100
	i = 0;
	for c in prenom:
		res[i] = ord(c)
		i += 1
	return res

def loadFile(fname, value):
	global data, values
	with open(fname, 'r') as f:
		line = f.readline()
		while line != '':
			line = line[:-1]
			data.append(toVector(line))
			values.append(value)
			line = f.readline()

loadFile('filles.txt', True)
loadFile('garcons.txt', False)

#print data
#print values
digest()
while True:
	sys.stdout.write('Prenom : ')
	prenom = sys.stdin.readline()[:-1]

	if compute(prenom):
		print '%s est une fille' % prenom
	else:
		print '%s est un garcon' % prenom
