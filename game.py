#Rishabh Shah
#2016
#States Game

import sys
import textwrap
import random

fh = open("StatesAndCapitals.txt", "r")
statesAndCapitals = []

for line in fh:
	line = line.strip()
	statesAndCapitals.append(line)

print ""
print textwrap.fill("Welcome to Rishabh's State Capitals Game! You will be given a state and you need to answer with the correct capital.")
print ""

while True:
	random.shuffle(statesAndCapitals)
	count = len(statesAndCapitals)
	for item in statesAndCapitals:
		parts = item.split(",")
		state = parts[1]
		capital = parts[0]
		while True:
			answer = raw_input("What is the capital of " + state + "?: ")
			if answer == capital:
				print "You got it correct!"
				break
			else:
				print "You got it wrong! Try again."
		while True:
			print ""
			playAgain = raw_input("Would you like to play another state?: ")
			if playAgain == "no" or playAgain == "n":
				print ""
				print "Goodbye"
				sys.exit()
			if playAgain == "yes" or playAgain == "y":
				print ""
				break
			if playAgain != "yes" or playAgain != "y" or playAgain != "no" or playAgain != "n":
				print "You entered something that does not compute. Please try again."
		count -= 1
		if count == 0:
			print ""
			print "You finished the game. Goodbye"
			sys.exit()