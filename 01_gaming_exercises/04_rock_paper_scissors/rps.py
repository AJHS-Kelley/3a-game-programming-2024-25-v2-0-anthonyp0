# Rock, Paper , Scissors by Anthony Pitts, v0.0

# MODULE IMPORTS
import random

# DATA STRUCTURES -- Player
playerScore= 0
playerName="Test Player"
playerChoice= None

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
playerName = input("Please type your name and press enter\n")
print(f"Hello {playerName}!\n")
isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()
print("isCorrect")

if isCorrect == "yes":
    print(f"Ok {playerName}, lets play rock, paper, scissors")
else:
    playerName = input("Please type your name and press enter\n")

    


