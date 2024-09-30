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
while loopCount < loopsReq:
 loopCount=0
 loopsReq= int(input("how many loops do you want\n enter an integer, no commas, and press enter.\n"))
# req is the universal abbreviation in computer programming for request. reqs = REQUESTS.
 rpsTimeStart= time.time() # returns the number of seconds since jan 01, 1970 @ 12:00am
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
numDraws+=1
else:
print("unable to determine a winner. please restart.")

loopCount+= 1

print(f"Your final score : {playerScore}\n Cpu Final score : {cpuScore}\n Draws : {numDraws}\n.")
if playerScore > cpuScore:
       print(f"Congratulations. a winner is you\n.")
elif cpuScore > playerScore:
      print(f"the cpu wins. you are a disappointment to all.\n")
else:
      print("Unable to determiner a winner.\n please restart.\n")
      exit()

rpsTimeStop= time.time()
rpsTime = rpsTimeStop - rpsTimeStart
print(f"Number of loops: {loopCount}.\n")
print(f"Execution Time {rpsTime:.2F}seconds.\n")

    
    # print the results to the screen
    # award point to winner and output results

