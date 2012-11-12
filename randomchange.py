#! /usr/bin/python

import random
import cPickle as pickle
import os.path

chords = ["E", "A", "D", "Emin", "Amin", "Dmin"]
numberOfChords = len(chords)
freqPath = "frequency.dat"

try:
	with open(freqPath) as f: frequency = pickle.load(f)
except IOError as e:
	frequency = dict()
	for i in range(0, numberOfChords - 1):
		for j in range(i + 1, numberOfChords):
			frequency[i, j] = 0

first = random.randint(0, numberOfChords - 2)
second = random.randint(0, numberOfChords - 1)

# Make sure that first < second
if first >= second:
	temp = second
	second = first
	first = second

# Make sure that first != second
if first == second:
	second = second + 1

print "Change: " + chords[first] + " <-> " + chords[second]

frequency[first, second] = frequency[first, second] + 1

with open(freqPath, 'w') as f:
	pickle.dump(frequency, f)
