from turtle import *
setup(1000,1000)
Screen()
title("Turtle Keys")
move = Turtle()
showturtle()

def w():
    move.forward(45)

def s():
    move.back(45)

def a():
    move.left(45)

def d():
    move.right(45)


onkey(w, "Up")
onkey(s, "Down") # "Back"
#         ^^^^
onkey(a, "Left")
onkey(d, "Right")

listen()
mainloop() 