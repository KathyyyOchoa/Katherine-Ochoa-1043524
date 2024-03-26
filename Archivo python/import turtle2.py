import turtle

t = turtle.Turtle()

t.speed(5)

t.shape("turtle")


t.penup()

t.goto(-100, 0)

t.pendown()

t.goto(-50, 50)

t.goto(50, -50)

t.goto(100, 0)

t.goto(50, 50)

t.goto(-50, -50)

t.goto(-100, 0)


t.penup()

t.goto(0, 50)

t.dot(25, 0, 0, 0)

t.goto(0, -50)

t.dot(25, 0, 0, 0)


t.penup()

t.goto(0,0)