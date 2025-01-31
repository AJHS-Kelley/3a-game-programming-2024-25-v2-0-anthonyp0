# Flow Control Structures, Anthony Pitts, v0.0
# Making Computer Programs Make Decisions

temperature = 75.34
color = "Red"
height = 6
likesPineappleOnPizza = True

# SINGLE DECISION POINT - if Statement
# if CONDITIONAL_EXPRESSION:<-- This will use a COMPARISON OPERATOR 99% of the time
       # runThisCode IF the CONDITIONAL_EXPRESSION is True

if temperature > 100:
    print("It is hot as the sun outside \n.")

if height >= 6:
    print(" They are above the height requirement.\n")

# CHEAT CODE FOR IF STATEMENTS THAT USE BOOLEANS.
if likesPineappleOnPizza:
    print("Yummy")
    
# What if we want something different to happen?
if color == "Red" :# COMMON ERRORS FOR STUDENTS IS USING = INSTEAD OF ==
     print("Your shirt is the correct uniform color. \n")
else: 
     print("Your shirt is not the correct uniform color \n")
weather = "Rainy"
if weather == "Rainy":
    print("Its the right weather")
else : 
      print("It is not the right weather")

