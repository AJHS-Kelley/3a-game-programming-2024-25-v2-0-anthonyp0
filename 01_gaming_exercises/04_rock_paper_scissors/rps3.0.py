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
# remove the lines of code that add score to player, cpu, or draws below.
def pickWinner(playerChoice: str, cpuChoice: str) -> str:
    """Determines the winner using player and CPU choices."""
    if playerChoice == "rock" and cpuChoice == "paper": 
        # CPU WINS 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
         
        return "cpu wins"
    elif playerChoice == "rock" and cpuChoice == "scissors": 
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
       
        return "player wins"
    elif playerChoice == "rock" and cpuChoice == "rock":
            # draw
            print(f"the cpu chose {cpuChoice} and you chose {playerChoice}\n")
            print("its a draw!\n")
            return "draw"
    elif playerChoice == "scissors" and cpuChoice == "rock":
        # Cpu wins
            print(f"the cpu chose {cpuChoice} and you chose {playerChoice}\n")
            print("the cpu wins a point")
            
            return "cpu wins"
    elif playerChoice == "scissors" and cpuChoice == "paper":
            # player wins
            print(f"the cpu chose {cpuChoice} and you chose {playerChoice}\n")
            print("you win a point\n")
            
            return "player wins"
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        # draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}\n")
        print("its a draw!\n")
    elif playerChoice == "paper" and cpuChoice == "rock":
        # player wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}\n")
        print("you win a point\n")
        
        return "player wins"
    elif playerChoice == "paper" and cpuChoice == "paper":
        # draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}\n")
        print("its a draw")
        return "draw"
    elif playerChoice == "paper" and cpuChoice == "scissors":
        # cpu wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}\n")
        print("the cpu wins\n")
        
        return "cpu wins"
    else:
        print("unable to determine a winner. please restart\n")
        exit()

def score(winner: str)-> int:
    """this function uses the winner to update the score for cpu, num, draws, and player score"""
    if winner == "player wins":
     score = 1
    elif winner == "cpu wins":
        score = 1
    else: # This is a DRAW. 
        score = 0
    return score

def matchWinner(playerScore: int, cpuScore: int) -> bool:
    """ this function detrmines if a player has won the game or not by scoring 5 points."""
    if playerScore >= 5:
        print("congratulations! you are the winner.\n")
        return True
    elif cpuScore>=5:
        print("sadly u lost to an bot.\n")
        return True
    else: # no winner yet
        return False
    
def playGame(playerScore:int , cpuScore: int)-> None:
    """ this function will use all other function to play rock , paper, scissors."""
    while True:
        cpuPick = cpuChoice()
        playerPick= playerChoice()
        roundWinner = pickWinner(playerPick, cpuPick)
        if roundWinner == "player wins":
            playerScore+=score(roundWinner)
        if roundWinner == "cpu wins":
            cpuScore += score(roundWinner)
        print(f"player score: {playerScore}\n")
        print(f"cpu score: {cpuScore}\n")


        if matchWinner(playerScore, cpuScore)== True:
            break
playGame(playerScore, cpuScore)