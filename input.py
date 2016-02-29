#Rishabh Shah
#2016
#States Game Input

import sys
import textwrap

print textwrap.fill("Welcome to the State Game input program. Please enter the states and the respective capitals. Your answers will be added to 'StatesAndCapitals.txt'.")
print ""

while True:
	state = raw_input("Please enter state: ")
	capital = raw_input("Please enter capital: ")

	print ""

	print capital + ", " + state
	while True:
		playAgain = raw_input("Would you like to add another state?: ")
		if playAgain == "no" or playAgain == "n":
			print ""
			print "Goodbye"
			sys.exit()
		if playAgain == "yes" or playAgain == "y":
			break
		if playAgain != "yes" or playAgain != "y" or playAgain != "no" or playAgain != "n":
			print "You entered something that does not compute. Please try again."
			print ""