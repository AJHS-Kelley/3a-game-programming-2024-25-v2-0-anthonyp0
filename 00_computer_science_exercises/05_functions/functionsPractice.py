# Functions Practice, Anthony Pitts, v0.0

import random
userChoice=None
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
    # print "Hello, World!" to the screen in that language.
    helloWorldMulti()
    print(f"English,Spanish,French")
    input(f"Hey User, pick a language. {userChoice}\n")

    userChoice = random.randint(0, 3) 
    if userChoice == 1:
        print("you have chosen english.\n")
    elif userChoice == 2:
        print("you have chosen spanish.\n")
    elif userChoice == 3:
        print("you have chosen french.\n")
    else:
        print("enter a number 1 through 3 to pick an language.\n")
        exit()