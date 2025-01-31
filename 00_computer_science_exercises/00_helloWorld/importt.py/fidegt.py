# import object from module turtle
from turtle import *

# intial state of spinner is null(stable)
state ={"turn":0}

# Draw fidegt spinner
def spin():
        clear()
    # angle of fidget spinner
        angle=state['turn']/5

# to rotate clockwise we use right
#for anticlockwise rotation we use lest
        right(angle)    
    #move the turtle foward by specified distance
        forward(100)

    #draw a dot with diameter 120 using colour red
        dot(120,'red')

    #move the turtle backward by specified distance
        back(100)
        "second dot"
        right(120)
        forward(100)
        dot(120,"blue")
        back(100)

        "third dot"
        right(120)
        forward(100)
        dot(120,"green")
        back(100)
        right(120)

        update()


#animate fidget spinner
def animate():
    if state['turn']>0:
            state['turn']-=1

    spin()
    ontimer(animate,10)

    #flick fidget spinner
def flick():
     state['turn']+=40 #accleration of spinner

#setup window screen
setup(600,400,370,0)
bgcolor("black")
    
tracer(False)

#wing of fidget spinner
width(60)
color("orange")

#keyboard key for the rotation of spinner
onkey(flick,'space')


listen()
animate()
done ()