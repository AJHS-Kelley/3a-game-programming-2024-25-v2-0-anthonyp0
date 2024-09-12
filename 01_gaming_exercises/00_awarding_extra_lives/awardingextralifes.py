# Awarding Extra Lifes, Anthony Pitts v0.0
playerScore = 0
highScore = 10000
lives = 3
name = "Anthony"
print(f"hello {name}! you scored {highScore} points. \n")





# Character Reference
# Curly Braces {}
# brackets []
# angle brackets <>
# parentheses ()

# Allow the user to input the score.

# if score is 10000 or less
  # Lose a Life
# If score is > 10000 but less than 100001
  # Give one extra life
# if score is > 100000
  # Give 2 Extra Lifes

# Output the score and number of lives to the screen.
if highScore <= 10000:

  print("You lost one life.\n")
elif highScore >= 10000:
   
   print("You have gained a new life!\n")
if highScore > 100000:
   
   print("You have earned two lifes! Lucky Son Of A Gun")

else: ("You have not gained a new life loser!\n")


  