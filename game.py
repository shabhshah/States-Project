#Rishabh Shah
#2016
#States Game

import sys
import textwrap
import random

def printScore():
	global score
	print"Your score is " + str(score) + "."

fh = open("StatesAndCapitals.txt", "r")
statesAndCapitals = []
score = 0
right = 0
wrong = 0
goodbye = textwrap.fill("You finished the game with a final score of " + str(score) \
					     + ". You got " + str(right) + " correct and " + str(wrong) + " incorrect.")

for line in fh:
	line = line.strip()
	statesAndCapitals.append(line)

random.shuffle(statesAndCapitals)
count = len(statesAndCapitals)

print ""
print textwrap.fill("Welcome to Rishabh's State Capitals Game! \
You will be given a state and you need to answer with the correct capital. \
A correct answer is worth 5 points and an incorrect answer is worth -10 points.")
print ""

for item in statesAndCapitals:
	parts = item.split(",")
	while True:
		answer = raw_input("What is the capital of " + parts[1] + "?: ")
		if answer == parts[0]:
			score += 5
			right += 1
			print "You got it correct!"
			printScore()
			break
		else:
			score -= 10
			wrong += 1
			print "You got it wrong!"
			printScore()
			break
	while True:
		print ""
		playAgain = raw_input("Would you like to play another state?: ")
		if playAgain == "no" or \
		   playAgain == "n":
			print ""
			print goodbye
			print ""
			print "Goodbye"
			sys.exit()
		elif playAgain == "yes" or \
			 playAgain == "y":
			print ""
			break
		else:
			print "You entered something that does not compute. Please try again."
	count -= 1
	if count == 0:
		print ""
		print goodbye
		print ""
		print "Goodbye"
		sys.exit()