# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Jason Klingman
# Creation Date: 7/26/2020
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time


def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()


def chooseCave():
	#not properly indented
	cave = ''
	while cave != '1' and cave != '2':
		#getting rid of redundant print statement
		cave = input('Which cave will you go into? (1 or 2)')
		#it needs to be cave instead of caves
	return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	#it says sleep for 2 seconds but listed 3
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)
	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		#missing () around the print statement
		print('Gobbles you down in one bite!')

playAgain = 'yes'
#needs to be playAgain == 'yes' or playAgain == y
#if you put in any capital letters it would exit the program
while playAgain.lower() == 'yes' or playAgain.lower() == 'y':
	displayIntro()
	#should be chooseCave instead of choosecave()
	caveNumber = chooseCave()
	checkCave(caveNumber)
    
	#getting rid of redundant print statement
	playAgain = input('Do you want to play again? (yes or no)')
	#making everything lower case from the input to make sure it matches
	#making it tell the user thanks for playing if it doesnt equal yes or y 
	if playAgain.lower != 'yes' or playAgain.lower() == 'y':
		#spelling error for playing
		print("Thanks for playing!")

