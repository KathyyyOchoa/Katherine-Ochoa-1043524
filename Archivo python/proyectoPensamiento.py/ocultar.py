from turtle import *

def restablecerTurtle():
    penup()
    goto(0,0)
    setheading(0)

    pendown()
    color("black")

def restablecerDibujo():
    restablecerTurtle()

    color("skyblue")
    penup()
    goto(-380,0)
    pendown()
    begin_fill()

    for i in range(2):
        forward(760)
        left(90)
        forward(280)
        left(90)
    end_fill()
     