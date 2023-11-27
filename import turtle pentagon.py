import turtle
from turtle import *

shape = input ("what shape do you want to make")
if shape == "square":
    # draw a square
    color("blue", "red")
    begin_fill()

    for i in range(0, 4):
        forward (50)
        right (90)
        end_fill()

    done()
elif shape == "triangle":
    # draw a triangle
     color("blue", "red")
     begin_fill()

     for i in range(0, 3):
        forward (50)
        right (120)
        end_fill()
        done()

elif shape == "pentagon":
    # draw a pentagon
    color("blue", "red")
    begin_fill()

    for i in range(0, 5):
        forward (50)
        right (72)
        end_fill()

    done()
    
else:
    print ("invalid shape")


    
