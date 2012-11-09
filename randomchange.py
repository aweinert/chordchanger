#! /usr/bin/python

import random

chords = {1: "E", 2: "A", 3: "D", 4: "Emin", 5: "Amin", 6: "Dmin"}

first = random.randint(1,6)
second = random.randint(1,5)

if second >= first:
	second = second + 1

print "Change: " + chords[first] + " <-> " + chords[second]
