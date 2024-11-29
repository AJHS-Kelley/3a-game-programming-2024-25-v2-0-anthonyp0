# Functions Practice, Anthony Pitts, v0.0

import random

def helloWorldMulti(): # FUNCTION SIGNATURE
    """This function will output Hello, World! in a language the user choose. """ # docstring \
    # print a list of languages to the screen, at least three but no more than five.
    print(""" 
    Welcome to the Hello , World! Translator
    The following languages are avaliable.
        1 [E]nglish
        2  [S]panish
        3 [F]rench



    """)
    # allow the user to select (input) a choice for the language.
    language = input("What language do you want?\n Please type 1 for english, 2 for spanish and 3 for french\n")
    if language == "1":
        print("Hello world!\n")
    elif language == "2":
        print("Hola Mundo!\n")
    elif language == "3":
        print("Salut tout le monde!\n")
    else:
        print("Please pick an number.\n")
        exit()

    # print "Hello, World!" to the screen in that language.
    #helloWorldMulti()


    # function to determine even / odd numbers
arguement1=random.randint(-1000,1000)

def isEven(arguement1:int) -> bool: # requires one argument (arguement1) and returns a boolean value.
    """determines if an integer value is even or odd."""
    if arguement1 % 2== 0:
        return True
    else:
        False

print(isEven(arguement1)) 

# function with multiple arguements
def canRideRollerCoaster(age: int, height: int)-> bool:
    if age > 10 and height > 4:
        print("you can ride.\n")
        return True
    else:
        print("you cannot ride.\n")
        return False
canRideRollerCoaster(4,10) # ARGUEMENTS MUST BE PASSED IN THE SAME ORDER AS THE FUNCTION SIGNATURE INDICATES.