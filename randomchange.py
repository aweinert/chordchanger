#! /usr/bin/python

import random
import cPickle as pickle
import os.path

numberOfChords = 6
freqPath = "frequency.dat"

try:
	with open(freqPath) as f: frequency = pickle.load(f)
except IOError as e:
	frequency = dict()
	for i in range(1, numberOfChords):
		for j in range(i + 1, numberOfChords + 1):
			frequency[i, j] = 0

chords = {1: "E", 2: "A", 3: "D", 4: "Emin", 5: "Amin", 6: "Dmin"}

first = random.randint(1, numberOfChords)
second = random.randint(1, numberOfChords - 1)

# Make sure that first < second
if first < second:
	second = second + 1
elif first >= second:
	temp = first
	first = second
	second = temp

print "Change: " + chords[first] + " <-> " + chords[second]

frequency[first, second] = frequency[first, second] + 1

with open(freqPath, 'w') as f:
	pickle.dump(frequency, f)
