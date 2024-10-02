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
# .lower() can turn ALL input into lowercase
# .upper() can turn ALL input into UPPERCASE

if isCorrect == "yes":
    print(f"Ok {playerName}, lets play rock, paper, scissors")
else:
    playerName = input("Please type your name and press enter\n")

# THE RULES using multi-line strings
print("""

Welcome to rock, paper , scissors bud!
its time to play rock, paper , scissors! Get ready!
You will play against the cpu. the first person to score five points wins.
you will select from rock, paper, scissors.
the cpu will select rock, paper, or scissors at random.
1) rock beats scissors
2) scissor beats paper
3) paper beats rock
""")   
# Multi-Line strings can be used as big comments
"""
Anything in between the sets of double-quotes is just ignored.
if you need to write large comments, its easier to use multi-line strings than puuting a # in front of 15 different lines.
"""
# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\n")
    print(f"the cpu has {cpuScore} points\n")
    playerChoice = input("Please enter rock, paper, or scissors and press enter\n").lower()
if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("Please enter rock, paper, or scissors and press enter\n").lower()
if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        print("you are not following my instructions. try again.")
        exit()
        
    
print(f" you have chosen {playerChoice}.\n")
else:

print(f" you have chosen {playerChoice}.\n")
    # print the current score for
    # let player select rock, paper, or scissors
    # let the cpu select rock, paper, or scissors
cpuChoice = random.randint(0, 2) # randomly select 0, 1 , or 2.
if cpuChoice == 0:
            cpuChoice = "rock"
elif cpuChoice == 1:
           cpuChoice = "scissors"
elif cpuChoice  == 2:
           cpuChoice = "paper"
else:
            print("Unable to determine CPU choice.\n Please restart.\n")
            exit()
print(f"CPU Choice: {cpuChoice}")
          
    # compare player choice to cpu choice
if playerChoice =="rock" and cpuChoice == "paper":
        # CPU wins
        print(f"The cpu chose {cpuChoice} and you chose {playerChoice}.\n")
elif playerChoice == "rock" and cpuChoice == "scissors":
        
    # Player wins
elif playerChoice == "rock" and cpuChoice == "rock":
    print(f"the cpu chose {cpuChoice} and you chose {playerChoice}")
    print(f"Tie. Go again")
         # Draw


elif playerChoice == "scissors"and cpuChoice == "rock":
     print(f"The cpu chose {cpuChoice} and you chose {playerChoice}.\n")
     print("The cpu scores a point.\n")
    # cpu wins 
elif playerChoice == "scissors"and cpuChoice == "paper":
    print(f"The cpu chose {cpuChoice} and you chose {playerChoice}.\n")
    print("the player scores a point.\n")
    # player wins
elif playerChoice == "rock"and cpuChoice == "scissors":
    print(f"the cpu choose {cpuChoice} and you chose {playerChoice}.\n")
    print("the player scores a point.\n")
    # player wins
    playerScore += 1
elif playerChoice == "rock" and cpuChoice == "rock":
    # DRAW 
 print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
print("its a draw!\n")
else:

print("unable to determine a winner. please restart.")

    
    # print the results to the screen
    # award point to winner and output results

