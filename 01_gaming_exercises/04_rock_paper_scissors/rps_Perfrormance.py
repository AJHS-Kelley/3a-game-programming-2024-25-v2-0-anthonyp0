# Rock, Paper , Scissors by Anthony Pitts, v0.0

# MODULE IMPORTS
import random, time

# DATA STRUCTURES -- Player
playerScore= 0
playerChoice= None
numDraws = 0
# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None




# THE RULES using multi-line strings

# Multi-Line strings can be used as big comments
"""
Anything in between the sets of double-quotes is just ignored.
if you need to write large comments, its easier to use multi-line strings than puuting a # in front of 15 different lines.
"""
# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
   
    # print the current score for
    # let player select rock, paper, or scissors
    # let the cpu select choice at random
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
            # let player select choice at random.
            
    print(f"CPU Choice: {cpuChoice}")
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
    # compare player choice to cpu choice
    if playerChoice =="rock" and cpuChoice == "paper":
        # CPU wins
        print(f"The cpu chose {cpuChoice} and you chose {playerChoice}.\n")
    elif playerChoice == "rock" and cpuChoice == "scissors":
        
    # Player wins
    elif playerChoice == "rock" and cpuChoice == "rock":
         print("Tie. Go again")
         
    # Draw
    elif # player chooses scissors, cpu chooses rock:
     print(f"The cpu chose {cpuChoice} and you chose {playerChoice}.\n")
     print("The cpu scores a point.\n")
    # cpu wins 
    elif # player choose scissors, cpu choose paper:
    print(f"The cpu chose {cpuChoice} and you chose {playerChoice}.\n")
    print("the player scores a point.\n")
    # player wins
     # player choose rock, cpu choose scissors:
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

