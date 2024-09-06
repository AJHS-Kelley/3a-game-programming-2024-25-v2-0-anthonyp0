# Data Types and Operators, Anthony Pitts, v0.0

# Fundamental Data Types
# String - str - Sequence of letters, numbers, spaces, or other characters.
# Strings in Python are inside ' ' or " "
# idc if you use ' ' or " " just be consistent.

# Boolean - bool - True or False values.

# Float - float - any number value with a decimal, +/-, including 0.

# Integers - int - any whole number, +/- including 0.

# Data types are stored in VARIABLES.
# A variable is bascially a bucket with a name to put data into.
# VARIABLE NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED IN IT.
# VARIABLES CANNOT START WITH A NUMBER.
# camelCaseVariablesNames
# snake_case_variable_names 

# DECLARING VARIABLES AND ASSIGNING VALUES

high_score = 600000 # int data type
highScore = 500000 #int data types

carSpeed = 20.75 # float data type, miles per hour
car_speed = 1.65772462 # float data type, miles per hour

hasAxe = True # boolean data type
isPurple = False # boolean data type

player_name = "Anthony Pitts" # string data type
enemy_type = "water" # string data type

# ASSIGN NEW VALUES
player_name = "Johnson Hillies"
car_speed = -1.25

# DATA TYPES CAN CHANGE, BE CAREFUL
hasAxe = 5.0

# Printing Data Types
newInt = 3
newFloat = 4.0
newString = "Skibidi Toilet"
newBool = False

print(type(newInt))
print(type(newFloat))
print(type(newString))
print(type(newBool))


# printing Variables to Console / screen 
print(player_name)
print(isPurple)
print(high_score)
print(car_speed)

# printing variables and expressions to console / screen
print(high_score + 3500)
print(4*12)
print(high_score)


# PRINTING VARIABLES INSIDE OF STRONG
print(f"Hello {player_name}. Your high score is {high_score}. \n")

# ARITHMETIC OPERATORS
myInt = 3
mtFloat = 2.57
myNum = 0

# addition
myInt = 3 + 54
myFloat = 2.0 + 3.25

myInt = myInt + 5

myNum = myInt + myFloat
# When you add an int and a float together, the answer becomes a float

# subtraction
myNum = myInt - myFloat
myInt = myFloat - 1.25

 # Multiplication
myNum = myInt * myFloat

# Division
myNumber = myInt / myFloat # first is numerator, second num is denominator

# MODULUS (MODULO) % -- Returns REMAINDER after dividing.
# MOST COMMON USE FOR MODULUS IS DETERMINING EVEN / ODD NUMBERS.
numStudents = 6
numSlicesPizza = 36

leftOvers = numSlicesPizza % numStudents
print(leftOvers)

# EXPONENTS *
numStudents = 5 ** 2 # 5 is the base, 2 is the exponent.

# FLOOR-DIVISION // -- Divides, throws out any decimal.
myNum = myInt // myFloat

# Addition-Assignment Operator - Mostly used for counters.
myNum = 5
myNum = myNum + 1 # Old-School Method
myNum += 1 # New Hotness
myNum*= 1
myNum /= 1 


# COMPARSION OPERATORS
# IS-EQUAL-TO== Are the two values equal to eachother?
# Returns true or false based on evaluation.
x = 12.0
print(x == 5)

# NOT-EQUAL-TO != Are the two values NOT equal?

print (x != 12)

# GREATER THAN / GREATER THAN-OR-EQUAL TO
print(5 > 3) # Greater Than
print(12 >= 2) # Greater Than or Equal To

# LESS THAN / LESS-THAN-OR-EQUAL TO
print(5 < 3) # LESS THAN
print(12 <= 2) # Less Than or Equal To

# LOGICAL OPERATORS
# and -- ALL CONDITIONS MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
age = 23
height = 72.4
eyeColor = "Brown"
# In order to ride the Teacups, you must be at least 18 years old and at least 60" tall.
print(age >= 18 and height >= 60)
print(age >= 18 and height >= 60)
# ALWAYS CHECK FOR THE MOST-LIKELY TO BE FALSE CONDITION FIRST!!
# print(defeatedBoss == True and level > 5 and hasBlueKey == True )


# or -- AT LEAST ONE CONDITION MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
print(age >= 18 and height >= 60)
print(age >= 18 and height >= 60 or eyeColor == "Brown")
# ALWAYS CHECK FOR THE MOST-LIKELY TO BE TRUE CONDITION FIRST!!
# print(defeatedBoss == False and level > 5 and hasBlueKey == True )

# not -- RETURNS THE OPPOSITE VALUE OF THE STATEMENT.
a = 9
print(a == 9)
print (not (a == 5))

# COMBINING LOGICAL OPERATORS
 # print(a == 5 and hasKey == True or isCloud == True)
# True and

# IDENTITY OPERATORS
g = 1.0
h = 1.0
i = g
print(g is h)
print(i is h)
print(i is not 1.0)
print(i is not g)

# MEMBERSHIP OPERATORS
fruits = ["apple", "banana", "tomato"]
print( "banana" in fruits)
print("potato" in fruits) 
