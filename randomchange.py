#! /usr/bin/python

import random
import cPickle as pickle
import os.path

chords = ["E", "A", "D", "Emin", "Amin", "Dmin"]
numberOfChords = len(chords)
scorePath = "score.dat"
variance = 1.0 # Play around with this value. The lower the value, the higher the probablity for lower-ranked chord combinations to be chosen

try:
	with open(scorePath) as f: score = pickle.load(f)
except IOError as e:
	score = dict()
	for i in range(0, numberOfChords - 1):
		for j in range(i + 1, numberOfChords):
			score[i, j] = 1

currentMax = float("-inf")
for i in range(0, numberOfChords - 1):
	for j in range(i + 1, numberOfChords):
		randomVal = random.gauss(1 / score[i, j], variance)
		if randomVal > currentMax:
			currentMax = randomVal
			first = i
			second = j

print "Change: " + chords[first] + " <-> " + chords[second]

newScore = int(raw_input("What is your current score for that chord change? "))

score[first, second] = (score[first, second] + newScore) / 2

with open(scorePath, 'w') as f:
	pickle.dump(score, f)
