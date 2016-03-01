#Rishabh Shah
#2016
#States Game Input

import sys
import textwrap

print textwrap.fill("Welcome to the State Game input program. Please enter the states and the respective capitals. Your answers will be added to 'StatesAndCapitals.txt'.")
print ""

fh = open("StatesAndCapitals.txt", "a")
a = """
"""

while True:
	state = raw_input("Please enter state: ")
	capital = raw_input("Please enter its capital: ")

	print capital + ", " + state

	fh.write(capital + "," + state)
	fh.write(a)

	print ""

	while True:
		playAgain = raw_input("Would you like to add another state?: ")
		if playAgain == "no" or playAgain == "n":
			print ""
			print "Goodbye"
			sys.exit()
		if playAgain == "yes" or playAgain == "y":
			print ""
			break
		if playAgain != "yes" or playAgain != "y" or playAgain != "no" or playAgain != "n":
			print "You entered something that does not compute. Please try again."
			print ""