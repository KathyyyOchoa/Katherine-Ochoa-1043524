import turtle

longitud =90
angulo =120

#turtle.showturtle
#selecciona el color de relleno
turtle.fillcolor('red')

#inicio de color de relleno
turtle.begin_fill()
#CUADRADO
#for i in range(4):
#  turtle.forward(longitud)
#  turtle.right(90)
turtle.circle(100)
#Fin de relleno
turtle.end_fill()

turtle.penup
turtle.goto(100,40)
turtle.pendown

#TRIANGULO
for i in range(4):
  turtle.forward(longitud)
  turtle.right(angulo)
  

#turtle.done