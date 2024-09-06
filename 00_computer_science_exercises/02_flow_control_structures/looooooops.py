# Loops , Anthony Pitts, v0.0
import random # import the random module for us to use
# generally put all your import statements at the top.
# TWO TYPES OF LOOPS
#for <-- Used when you know how many loops you'll need.
# while <-- Used when you do not know how many loops you'll need.

# for loop is like Go Fish, you search each card for what player asked.
# while loop is like musical chairs, you move around until the music stops.

# EACH TRIP THROUGH THE ENTIRE LOOP IS CALLED AN iteration
# "iterate through the list" means use a for loop.

# for loop Example -- Iterating a list
fruits = ["apple" , "banana", "strawberry", "tomato"]
for eachFruit in fruits:
    print(eachFruit)
# continue Keyword -- Skips the current iteration and then finishes the loop.
fruits = ["apple" , "banana", "strawberry", "tomato"]
for eachFruit in fruits:
    if eachFruit == "banana":
        continue
    print(eachFruit)


# break Keyword -- Immediately exit the loop.
fruits = ["apple" , "banana", "strawberry", "tomato"]
for eachFruit in fruits:
    if eachFruit == "banana":
        break
    print(eachFruit)
# for loops using range().  range(x) is EXCLUSIVE, it starts at 0 ands ends at x - 1
    for i in range(10): # range is 0 - 9
        print (i)


# Might not always want to start at zero.
for i in range(10,100): #
    print(i)

# Not want to count by 1
    for i in range(10,100,5): # 10 = start, 100 - 1 = stop, 5 = # to count by
        print(i)

# sometimes you're not done writing the loops
        for x in range(10):
            pass # tells python this loop isnt finished, dont freak out.

# while loops -- musical chairs
playerScore = 0
while playerScore < 100: # run as long as this is true
    playerScore += random.randint(1,3)
    print(f"Starting : {playerScore}")
playerScore += random.randint(1,3)
print(f" After: {playerScore}")
