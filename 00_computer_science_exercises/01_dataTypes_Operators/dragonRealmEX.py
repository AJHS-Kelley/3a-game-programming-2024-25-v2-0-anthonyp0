# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time
import datetime

# saving data to a file
# step 1 -- create the file name to use
#logFileName = "dragonrealmlog" + str(time.time()) + ".txt"
logFileName = "dragonrealmlog.txt"
# ex dragonrealmlog1132am.txt 

# step 2 -- create / open the file to save the data
saveData = open(logFileName, "a")
# file modes
# "x" creates file, if file exists, exit with error message
# "w" creates file, if file exists, erase and overwrite file contents
# "a" creates file. if file exists, append data to the file

saveData.write("game started" + " " + str(datetime.datetime.now()) + "\n")


def displayIntro():

    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()







# item data
itemSelected = 0
numItems = 0
