from ocultar import *

def dibujarFuncion(contador, rgb):
    restablecerTurtle()

    if contador == 0:
        dibujo0(rgb)
    elif contador == 1:
        dibujo1(rgb)
    elif contador == 2:
        dibujo2(rgb)
    elif contador == 3:
        dibujo3(rgb)
    elif contador == 4:
        dibujo4(rgb)
   




def dibujo0(rgb):
    
    import turtle
    restablecerTurtle()
    restablecerDibujo() 

    # Configuración inicial
    screen = turtle.Screen()
    screen.setup(width=800, height=600)

    # Función para dibujar un rectángulo
    def draw_rectangle(x, y, width, height, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        for _ in range(2):
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)
        turtle.end_fill()

    # Función para dibujar un círculo
    def draw_circle(x, y, radius, color):
        turtle.penup()
        turtle.goto(x, y - radius)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        turtle.circle(radius)
        turtle.end_fill()

    # Función para dibujar un pentágono
    def draw_pentagon(x, y, size, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(72)
        turtle.end_fill()

    # Función para dibujar un triángulo
    def draw_triangle(x, y, size, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
        turtle.end_fill()

    # Dibujar el fondo
    def draw_background():
        # Dibujar el sol
        draw_circle(300, 240, 25, "yellow")
        
        # Dibujar el césped (más oscuro)
        draw_rectangle(-380, 0, 760, 50, "#006400")  # Cambiando el color a verde oscuro
        
        # Dibujar el tronco del árbol
        draw_rectangle(-20, 20, 30, 100, "brown")
        
        # Dibujar las hojas del árbol
        draw_triangle(-65, 50, 120, "green")
        draw_triangle(-70, 100, 130, "green")
        draw_triangle(-65, 130, 120, "green")

    # Dibujar la cara del árbol
    def draw_face():
        # Dibujar los ojos
        draw_pentagon(0, 50, 5, "black")
        draw_pentagon(-10, 50, 5, "black")
        
        # Dibujar la boca
        turtle.penup()
        turtle.goto(-10, 40)
        turtle.pendown()
        turtle.setheading(-60)
        turtle.circle(10, 120)

    def draw_face_1():
        # Dibujar los ojos
        draw_pentagon(-140, 45, 5, "black")
        draw_pentagon(-150, 45, 5, "black")
        
        # Dibujar la boca
        turtle.penup()
        turtle.goto(-155, 30)
        turtle.pendown()
        turtle.setheading(-60)
        turtle.circle(15, 120)

    # Función para dibujar un arbusto
    def draw_bush(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color("#228B22")  # Verde oscuro
        turtle.begin_fill()
        for _ in range(3):
            turtle.circle(30, 120)
            turtle.left(120)
        turtle.end_fill()

    # Dibujar el fondo
    draw_background()

    # Dibujar la cara del árbol
    draw_face()

    # Dibujar la roca
    draw_circle(-130, 50, 30, "gray")
    draw_circle(-110, 40, 20, "darkgray")
    draw_face_1()

    # Dibujar un arbusto
    draw_bush(290, 2)
    draw_bush(-280, 4)

    restablecerTurtle()

    # Ocultar la pluma y finalizar
    turtle.hideturtle()


def dibujo1(rgb):
    import turtle

    restablecerTurtle()
    restablecerDibujo()

    # Configuración inicial
    screen = turtle.Screen()
    screen.setup(width=800, height=600)

    # Función para dibujar un rectángulo
    def draw_rectangle(x, y, width, height, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        for _ in range(2):
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)
        turtle.end_fill()

    # Función para dibujar un círculo
    def draw_circle(x, y, radius, color):
        turtle.penup()
        turtle.goto(x, y - radius)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        turtle.circle(radius)
        turtle.end_fill()

    # Función para dibujar un pentágono
    def draw_pentagon(x, y, size, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(72)
        turtle.end_fill()

    # Función para dibujar un triángulo
    def draw_triangle(x, y, size, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
        turtle.end_fill()

    # Dibujar el fondo
    def draw_background():
        # Dibujar el sol
        draw_circle(300, 240, 25, "yellow")
        
        # Dibujar el césped (más oscuro)
        draw_rectangle(-380, 0, 760, 50, "#006400")  # Cambiando el color a verde oscuro
        
        # Dibujar el tronco del árbol
        draw_rectangle(-20, 20, 30, 100, "brown")
        
        # Dibujar las hojas del árbol
        draw_triangle(-65, 50, 120, "green")
        draw_triangle(-70, 100, 130, "green")
        draw_triangle(-65, 130, 120, "green")

    # Dibujar la cara del árbol
    def draw_face():
        # Dibujar los ojos
        draw_pentagon(0, 50, 5, "black")
        draw_pentagon(-10, 50, 5, "black")
        
        # Dibujar la boca
        turtle.penup()
        turtle.goto(-10, 40)
        turtle.pendown()
        turtle.setheading(-60)
        turtle.circle(10, 120)

    def draw_face_1():
        # Dibujar los ojos
        draw_pentagon(-140, 45, 5, "black")
        draw_pentagon(-150, 45, 5, "black")
        
        # Dibujar la boca
        turtle.penup()
        turtle.goto(-155, 30)
        turtle.pendown()
        turtle.setheading(-60)
        turtle.circle(15, 120)

    # Función para dibujar una pequeña flor
    def draw_flower(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color("red")
        turtle.begin_fill()
        for _ in range(6):
            turtle.circle(5)
            turtle.left(60)
        turtle.end_fill()

    # Función para dibujar un arbusto
    def draw_bush(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color("#228B22")  # Verde oscuro
        turtle.begin_fill()
        for _ in range(3):
            turtle.circle(30, 120)
            turtle.left(120)
        turtle.end_fill()

    # Dibujar el fondo
    draw_background()

    # Dibujar la cara del árbol
    draw_face()

    # Dibujar la roca
    draw_circle(-130, 50, 30, "gray")
    draw_circle(-110, 40, 20, "darkgray")
    draw_face_1()

    # Dibujar algunas florecitas a la derecha del árbol
    draw_flower(220, 50)
    draw_flower(130, 15)
    draw_flower(180, 35)
    draw_flower(120, 50)
    draw_flower(90, 25)
    draw_flower(250, 15)

    # Dibujar un arbusto
    draw_bush(290, 2)
    draw_bush(-280, 4)

    restablecerTurtle()

    # Ocultar la pluma y finalizar
    turtle.hideturtle()
    

def dibujo2(rgb):
    import turtle

    restablecerTurtle()
    restablecerDibujo()

    # Configuración inicial
    screen = turtle.Screen()
    screen.setup(width=800, height=600)

    # Función para dibujar un rectángulo
    def draw_rectangle(x, y, width, height, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        for _ in range(2):
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)
        turtle.end_fill()

    # Función para dibujar un círculo
    def draw_circle(x, y, radius, color):
        turtle.penup()
        turtle.goto(x, y - radius)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        turtle.circle(radius)
        turtle.end_fill()

    # Función para dibujar un pentágono
    def draw_pentagon(x, y, size, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(72)
        turtle.end_fill()

    # Función para dibujar un triángulo
    def draw_triangle(x, y, size, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
        turtle.end_fill()

    # Dibujar el fondo
    def draw_background():
        # Dibujar el sol
        draw_circle(300, 240, 25, "orange")
        
        # Dibujar el césped (más oscuro)
        draw_rectangle(-380, 0, 760, 50, "#996633")  # Cambiando el color a verde oscuro
        
        # Dibujar el tronco del árbol
        draw_rectangle(-20, 20, 30, 100, "brown")
        
        # Dibujar las hojas del árbol
        draw_triangle(-65, 50, 120, "darkorange")
        draw_triangle(-70, 100, 130, "darkorange")
        draw_triangle(-65, 130, 120, "darkorange")

    # Dibujar la cara del árbol
    def draw_face():
        # Dibujar los ojos
        draw_pentagon(0, 50, 5, "black")
        draw_pentagon(-10, 50, 5, "black")
        
        # Dibujar la boca
        turtle.penup()
        turtle.goto(-10, 40)
        turtle.pendown()
        turtle.setheading(-60)
        turtle.circle(10, 120)

    def draw_face_1():
        # Dibujar los ojos
        draw_pentagon(-140, 45, 5, "black")
        draw_pentagon(-150, 45, 5, "black")
        
        # Dibujar la boca
        turtle.penup()
        turtle.goto(-155, 30)
        turtle.pendown()
        turtle.setheading(-60)
        turtle.circle(15, 120)


    # Función para dibujar un arbusto
    def draw_bush(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color("#734d26")  # Verde oscuro
        turtle.begin_fill()
        for _ in range(3):
            turtle.circle(30, 120)
            turtle.left(120)
        turtle.end_fill()

    # Funión para dibujar una manzana
    def draw_apple(x, y, size, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)

        # Dibujar el cuerpo de la manzana
        turtle.circle(size)  # Cuerpo redondeado de la manzana

        # Dibujar el tallo
        turtle.penup()
        turtle.goto(x, y + size)  # Posición del extremo superior del cuerpo de la manzana
        turtle.pendown()
        turtle.setheading(90)  # Orientación hacia arriba
        turtle.color("brown")  # Tallo marrón
        turtle.forward(size * 0.4)  # Longitud del tallo
        turtle.right(90)  # Orientación hacia la derecha
        turtle.forward(size * 0.2)  # Ancho del tallo
        turtle.backward(size * 0.4)  # Retroceder al punto inicial
        turtle.end_fill()

    # Dibujar el fondo
    draw_background()

    # Dibujar la cara del árbol
    draw_face()

    # Dibujar la roca
    draw_circle(-130, 50, 30, "gray")
    draw_circle(-110, 40, 20, "darkgray")
    draw_face_1()

    # Dibujar un arbusto
    draw_bush(290, 2)
    draw_bush(-280, 4)

    # Dibujar manzanas.
    draw_apple(55, 5, 10, "Red")
    draw_apple(-10, 4, 10, "Red")
    restablecerTurtle()

    # Ocultar la pluma y finalizar
    turtle.hideturtle()

def dibujo3(rgb):
    import turtle

    restablecerTurtle()
    restablecerDibujo()

    # Configuración inicial
    screen = turtle.Screen()
    screen.setup(width=800, height=600)


    # Función para dibujar un rectángulo
    def draw_rectangle(x, y, width, height, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        for _ in range(2):
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)
        turtle.end_fill()

    # Función para dibujar un círculo
    def draw_circle(x, y, radius, color):
        turtle.penup()
        turtle.goto(x, y - radius)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        turtle.circle(radius)
        turtle.end_fill()

    # Función para dibujar un pentágono
    def draw_pentagon(x, y, size, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(72)
        turtle.end_fill()

    # Función para dibujar un triángulo
    def draw_triangle(x, y, size, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
        turtle.end_fill()

    # Dibujar el fondo
    def draw_background():
        # Dibujar el sol
        draw_circle(300, 240, 25, "yellow")
        
        # Dibujar el césped (más oscuro)
        draw_rectangle(-380, 0, 760, 50, "#006400")  # Cambiando el color a verde oscuro
        
        # Dibujar el tronco del árbol 
        draw_rectangle(-20, 20, 30, 100, "brown")  # Ajuste de posición del tronco
        
        # Dibujar las hojas del árbol (blancas para el invierno)
        draw_triangle(-65, 50, 120, "white")
        draw_triangle(-70, 100, 130, "white")
        draw_triangle(-65, 130, 120, "white")

    # Dibujar la cara del árbol
    def draw_face():
        # Dibujar los ojos
        draw_pentagon(0, 50, 5, "black")
        draw_pentagon(-10, 50, 5, "black")
        
        # Dibujar la boca
        turtle.penup()
        turtle.goto(-10, 40)
        turtle.pendown()
        turtle.setheading(-60)
        turtle.circle(10, 120)

    # Dibujar el muñeco de nieve
    def draw_snowman():
        # Cuerpo
        draw_circle(300, 70, 35, "white")
        draw_circle(290, 100, 25, "white")
        draw_circle(285, 120, 20, "white")
        
        # Ojos (pentágonos)
        draw_pentagon(255, 121, 5, "black")
        draw_pentagon(270, 121, 5, "black")
        
        # Nariz
        turtle.penup()
        turtle.goto(266, 119)
        turtle.pendown()
        turtle.setheading(240)
        turtle.color("orange")
        turtle.begin_fill()
        turtle.forward(6)
        turtle.left(120)
        turtle.forward(6)
        turtle.left(120)
        turtle.forward(6)
        turtle.end_fill()

    # Dibujar el fondo
    draw_background()

    # Dibujar la cara del árbol
    draw_face()

    # Dibujar el muñeco de nieve
    draw_snowman()

    
    restablecerTurtle()

    # Ocultar la pluma y finalizar
    turtle.hideturtle()

def dibujo4(rgb):
    import turtle
    restablecerTurtle()
    restablecerDibujo()
    # Configuración inicial
    screen = turtle.Screen()
    screen.setup(width=800, height=600)

    # Función para dibujar un rectángulo
    def draw_rectangle(x, y, width, height, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        for _ in range(2):
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)
        turtle.end_fill()

    # Función para dibujar un círculo
    def draw_circle(x, y, radius, color):
        turtle.penup()
        turtle.goto(x, y - radius)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        turtle.circle(radius)
        turtle.end_fill()

    # Función para dibujar un ovalo
    def draw_oval(x, y, width, height, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        turtle.left(45)
        for _ in range(2):
            turtle.circle(width/2, 90)
            turtle.circle(height/2, 90)
        turtle.end_fill()

    # Función para dibujar un pentágono
    def draw_pentagon(x, y, size, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        for _ in range(5):
            turtle.forward(size)
            turtle.right(72)
        turtle.end_fill()

    # Función para dibujar un triángulo
    def draw_triangle(x, y, size, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
        turtle.end_fill()

    # Dibujar el fondo
    def draw_background():
        # Dibujar el sol
        draw_circle(300, 240, 25, "yellow")
        
        # Dibujar el césped (más oscuro)
        draw_rectangle(-380, 0, 760, 50, "#006400")  # Cambiando el color a verde oscuro 
        
        # Dibujar el tronco del árbol (movido hacia la derecha)
        draw_rectangle(-30, 20, 30, 100, "brown")  # Ajuste de posición del tronco
        
        # Dibujar las hojas del árbol (blancas para el invierno)
        turtle.color("white")
        draw_triangle(-75, 50, 120, "white")
        draw_triangle(-80, 100, 130, "white")
        draw_triangle(-75, 130, 120, "white")

    # Dibujar la cara del árbol
    def draw_face():
        # Dibujar los ojos
        draw_pentagon(-10, 50, 5, "black")
        draw_pentagon(-20, 50, 5, "black")
        
        # Dibujar la boca
        turtle.penup()
        turtle.goto(-20, 40)
        turtle.pendown()
        turtle.setheading(-60)
        turtle.circle(10, 120)

    # Dibujar el charco de agua
    def draw_puddle(x, y, width, height, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        turtle.left(45)
        for _ in range(2):
            turtle.circle(width/2, 90)
            turtle.circle(height/2, 90)
        turtle.end_fill()

    # Función para dibujar los ojos del charco
    def draw_eyes(x, y):
        # Ojos (pentágonos)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.setheading(0)
        draw_pentagon(x, y, 5, "black")  # Ojo negro

    # Función para dibujar la boca del charco
    def draw_mouth(x, y):
        # Boca
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.setheading(135)
        turtle.circle(5, -180)

    # Dibujar el fondo
    draw_background()

    # Dibujar la cara del árbol
    draw_face()

    # Dibujar el charco de agua más grande
    draw_puddle(160, 12, 100, 15, "blue")

    # Dibujar los ojos del charco
    draw_eyes(120, 35)
    draw_eyes(130, 35)

    # Dibujar la boca del charco
    draw_mouth(130, 20)

    restablecerTurtle()
    # Ocultar la pluma y finalizar
    turtle.hideturtle()
    turtle.done()
    