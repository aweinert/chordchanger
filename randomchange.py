#! /usr/bin/python

import random
import cPickle as pickle
import os.path

# Configuration
chords = ["E", "A", "D", "Emin", "Amin", "Dmin"] # The chords from which combinations may be formed
scorePath = "score.dat" # Where to store the scores
variance = 0.05 # Play around with this value. The lower the value, the higher the probablity for lower-ranked chord combinations to be chosen

numberOfChords = len(chords)

# Load scores or initialize new score table, if none is found
try:
	with open(scorePath) as f: score = pickle.load(f)
except IOError as e:
	score = dict()
	for i in range(0, numberOfChords - 1):
		for j in range(i + 1, numberOfChords):
			score[i, j] = 1 # Use 1 as standard value, since otherwise 1 / score would lead to division by zero

# Get one random number for each chord change, use the change with the highest random number
# Since the expected value of the random number is 1/score, this gives us a higher probability for chords with lower scores
currentMax = float("-inf")
for i in range(0, numberOfChords - 1):
	for j in range(i + 1, numberOfChords):
		randomVal = random.gauss(1 / score[i, j], variance)
		if randomVal > currentMax:
			currentMax = randomVal
			first = i
			second = j

# Display the chord and update the score for it
print "Change: " + chords[first] + " <-> " + chords[second]
newScore = int(raw_input("What is your current score for that chord change? "))
# Weigh the new score and the previous average the same. This way older scores become "forgotten"
score[first, second] = (score[first, second] + newScore) / 2

# Display the score list
print ""
print "-----------------------------"
print "Your current average scores:"
for i in range(0, numberOfChords - 1):
	for j in range(i + 1, numberOfChords):
		print "\t"  + chords[i] + " <-> " + chords[j] + ": " + str(score[i,j])

# Save the new scores
with open(scorePath, 'w') as f:
	pickle.dump(score, f)
