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
def playerName() -> str: # function signature -- name of function, (arguements if any)
    """gets the name from the player and then returns it """
    # the line above is called a docstring, it gives a brief example of what the function does
    playerName = input("Please type your name and press enter\n")
    print(f"Hello {playerName}!\n")
    isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()
    if isCorrect == "yes":
        print(f"Ok {playerName}, lets play rock, paper, scissors")
    else:
        playerName = input("Please type your name and press enter\n")
    return playerName

# Calling the function
playerName = playerName()

# THE RULES using multi-line strings
def rules(): None
""" this function prints the rules for rock paper and scissors"""
print(f"""

        Welcome, {playerName} to rock, paper , scissors bud!
        its time to play rock, paper , scissors! Get ready!
        You will play against the cpu. the first person to score five points wins.
        you will select from rock, paper, scissors.
        the cpu will select rock, paper, or scissors at random.
        1) rock beats scissors
        2) scissor beats paper
        3) paper beats rock
        """)
        # does another part of this program need to access this information?
        # if yes you must have a return statement
        # if no a return statement is not required


def playerChoice() -> str:
    """ allows the player to choose rock paper or scissors"""
    print(f"the cpu has {cpuScore} points\n")
    playerChoice = input("Please enter rock, paper, or scissors and press enter\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("Please enter rock, paper, or scissors and press enter\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        print("you are not following my instructions. try again.")
        print(f" you have chosen {playerChoice}.\n")
        exit()
    else: 
        print(f" you have chosen {playerChoice}.\n")
    return playerChoice

def cpuChoice():
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
    return cpuChoice

def pickWinner(playerChoice: str, cpuChoice: str) -> str:
 """Determines the winner using player and CPU choices."""
    if playerChoice == "rock" and cpuChoice == "paper": 
 # CPU WINS 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1  
        return "CPU Wins"
    elif playerChoice == "rock" and cpuChoice == "scissors": 
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1 
        return "Player wins"
    elif playerChoice == "rock" and cpuChoice == "rock"
        # draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}\n")
        print("its a draw!\n")
        return "draw"
    elif playerChoice == "scissors" and cpuChoice == "rock"
    # Cpu wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}\n")
        print("the cpu wins a point")
        cpuScore += 1
    return "cpu wins"
    elif playerChoice == "scissors" and cpuChoice == "paper"
        # player wins
    print(f"the cpu chose {cpuChoice} and you chose {playerChoice}\n")
    print("you win a point\n")
    playerScore+=1
    return "player wins"
    elif playerChoice == "scissors" and cpuChoice == "scissors"
    # draw
    print(f"the cpu chose {cpuChoice} and you chose {playerChoice}\n")
    print("its a draw!\n")
    elif playerChoice == "paper" and cpuChoice == "rock"
    # player wins
    print(f"the cpu chose {cpuChoice} and you chose {playerChoice}\n")
    print("you win a point/n")
    playerScore+=1
    return "player wins"
    elif playerChoice == "paper" and cpuChoice == "paper"
    # draw
    print(f"the cpu chose {cpuChoice} and you chose {playerChoice}\n")
    print("its a draw")
    return "draw"
    elif playerChoice == "paper" and cpuChoice == "scissors"
    # cpu wins
    print(f"the cpu chose {cpuChoice} and you chose {playerChoice}\n")
    print("the cpu wins\n")
    cpuScore+=1
    return "cpu wins"
    else:
    print("unable to determine a winner. please restart\n")
    exit()

def score(winner: str)-> int:
"""this function uses the winner to update the score for cpu, num, draws, and player score"""
if winner == "Player Wins":
score = 1
elif winner == "CPU Wins":
score = 1
else: # This is a DRAW. 
score = 0
 return score

# MAIN GAME LOOP 
 while playerScore < 5 and cpuScore < 5: 
 print(f"{playerName} you have {playerScore} points.\nThe CPU has {cpuScore} points.\n") 
 


 print(f"Your Final Score: {playerScore}\nCPU Final Score: {cpuScore}\n")
 if playerScore > cpuScore: 
    print(f"Congratulations {playerName}, a winner is you!\n")
 elif cpuScore > playerScore: 
    print(f"The CPU wins. You are a disappointment to all.\n")
 else: 
    print("Unable to determine a winner.\nPlease restart.\n")
    exit()
# MAIN GAME LOOP
    while playerScore < 5 and cpuScore < 5:
        print(f"{playerName} you have {playerScore} points.\n")
    

 # print(f"CPU Choice: {cpuChoice}")
          
    # compare player choice to cpu choice
    if playerChoice =="rock" and cpuChoice == "paper":
        # CPU wins
        print(f"The cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        cpuScore+=1
    elif playerChoice == "rock" and cpuChoice == "scissors":
       # player wins
       print(f"The cpu chose {cpuChoice} and you chose {playerChoice}.\n")
       playerScore+=1
    elif playerChoice == "rock" and cpuChoice == "rock":
    # draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}")
        print(f"Draw! Try again.")
         
    elif playerChoice == "scissors"and cpuChoice == "rock":
     # cpu wins 
        print(f"The cpu chose {cpuChoice} and you chose {playerChoice}.\n")
    print("The cpu scores a point.\n") 
    cpuScore+=1

    elif playerChoice == "scissors"and cpuChoice == "paper":
    # player wins 
    print(f"The cpu chose {cpuChoice} and you chose {playerChoice}.\n")
    print("the player scores a point.\n")
    playerScore+=1
    
    elif playerChoice == "scissors"and cpuChoice == "scissors":
    print(f"the cpu choose {cpuChoice} and you chose {playerChoice}.\n")
    print("Draw! Try again.\n")
    
elif playerChoice == "paper" and cpuChoice == "rock":
  # player wins
    print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
print("the player wins a point\n")
playerScore+=1

elif playerChoice == "paper" and cpuChoice == "paper":
# draw
print(f"the cpu chose {cpuChoice} and the player chose {playerChoice}.\n")
    print("its a draw. try again.\n")
    elif playerChoice == "paper" and cpuChoice == "scissors":
    print(f" the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
    print("the cpu wins a point.\n")
    cpuScore+=1
    else:
    print("unable to determine winner. please restart.\n")
    exit()   
    print(f"your final score : {playerScore}\n cpu final score : {cpuScore}\n")
    if playerScore > cpuScore:
        print(f"congratulations {playerName}, heres your w!\n")
    elif cpuScore > playerScore:
        print(f"the cpu wins. you are such a loser.\n")
    else:
        print("unable to determine a winner.\n please restart.\n")
        exit()


    
    # print the results to the screen
    # award point to winner and output results

