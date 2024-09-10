# Awarding Extra Lifes, Anthony Pitts v0.0

highScore = 1000
lives = 3
high_score = 10000

# Allow the user to input the score.

# if score is 1000 or less
  # Lose a Life
# If score is > 10000 but less than 10001
  # Give one extra life
# if score is > 100000
  # Give 2 Extra Lifes

# Output the score and number of lives to the screen.
if highScore <= 1000:
  print("You lost one life")
if high_score >= 10000:
   print("You have gained a new life")
else: 