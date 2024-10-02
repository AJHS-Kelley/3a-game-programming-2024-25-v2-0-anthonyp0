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



# MAIN GAME LOOP
while loopCount < loopsReq:
 loopCount=0
 loopsReq= int(input("how many loops do you want\n enter an integer, no commas, and press enter.\n"))
# req is the universal abbreviation in computer programming for request. reqs = REQUESTS.
 rpsTimeStart= time.time() # returns the number of seconds since jan 01, 1970 @ 12:00am
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
        print("Unable to determine Cpu choice.\n Please Restart.")
        exit()
playerChoice = random.randint(0,2) # randomly select 0,1, or 2.
if playerChoice == 0:
            playerChoice = "rock"
elif playerChoice == 1:
           playerChoice = "scissors"
elif playerChoice  == 2:
           playerChoice = "paper"
else:
        print("Unable to determine Cpu choice.\n Please Restart.")
        exit()

    # compare player choice to cpu choice
if playerChoice == "rock" and cpuChoice == "paper":
        # CPU WINS
    print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
    print(" the cpu scores a point.\n")
    # cpuScore += 1
    cpuScore = cpuScore + 1
elif playerChoice == "rock " and cpuScore == "scissors":
        # player wins
        print(f"The cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point brodie.\n")
        playerScore += 1
elif playerChoice == "rock" and cpuChoice == "rock":
        # draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("its a draw.\n")
        numDraws +=1 
elif playerChoice == "scissors" and cpuChoice == "rock":
        # cpu wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point.\n")
        cpuScore +=1
elif playerChoice == "scissors" and cpuChoice == "paper":
        # player wins
        print(f"the cpu chose {cpuChoice}and you chose{playerChoice}.\n")
        print("you win a ppoint brodie.\n")
        playerScore+=1
elif playerChoice == "scissors" and cpuChoice == "scissors":
        # draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("its a draw!.\n")
        numDraws+=1
elif playerChoice=="paper" and cpuChoice=="rock":
        #player wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point brodie.\n")
        playerScore+=1
elif playerChoice=="paper" and cpuChoice == "paper":
        # draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("its a draw.\n")
        numDraws+=1
elif playerChoice=="paper" and cpuChoice == "scissors":
        #CPU wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point.\n")
        cpuScore+=1
else:
        print("unable to determine a winner. please restart.\n")
        exit()
        loopCount +=1

print(f"your final score: {playerScore}\n cpu final score:{cpuScore}\n Draws:{numDraws}\n")
if playerScore > cpuScore:
        print(f"congratulations you won!\n")
elif cpuScore>playerScore:
        print(f"the cpu wins. you suck.\n")
else:
        print("unable to determine a winner.\n please restart.\n")
        exit()        

rpsTimeStop = time.time()
rpsTime = rpsTimeStop - rpsTimeStart
print(f"Number of  loops: {loopCount}\n")
print(f"Execution Time {rpsTime:2F} seconds\n")
