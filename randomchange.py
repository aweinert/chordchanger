#! /usr/bin/python

import random
import cPickle as pickle
import os.path

chords = ["E", "A", "D", "Emin", "Amin", "Dmin"]
numberOfChords = len(chords)
scorePath = "score.dat"

try:
	with open(scorePath) as f: score = pickle.load(f)
except IOError as e:
	score = dict()
	for i in range(0, numberOfChords - 1):
		for j in range(i + 1, numberOfChords):
			score[i, j] = 1

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

newScore = int(raw_input("What is your current score for that chord change? "))

score[first, second] = (score[first, second] + newScore) / 2

with open(scorePath, 'w') as f:
	pickle.dump(score, f)
