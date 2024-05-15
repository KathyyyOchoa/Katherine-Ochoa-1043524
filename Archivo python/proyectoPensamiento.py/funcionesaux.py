from turtle import *
from ocultar import *
from cuento import *
from dibujo import * 

ListaCuento = []

contadorPasos=0



def rectanguloDibujo():
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
    
def rectanguloTexto():
    restablecerTurtle()

    color("white")
    penup()
    goto(-380, -100)
    pendown()
    begin_fill()

    for i in range(2):
        forward(760)
        right(90)
        forward(180)
        right(90)
        
    end_fill()

def dibujarCuadros():
    restablecerTurtle()
    penup()
    goto(-320, -80)
    pendown()
    color("black")
    left(90)

    begin_fill()
    for i in range(2):
        forward(70)
        left(90)
        forward(60)
        left(90)
    end_fill()
    
    restablecerTurtle()
    penup()
    goto(320, -80)
    pendown()
    color("black")
    left(90)
    begin_fill()
    for i in range(2):
        forward(70)
        right(90)
        forward(60)
        right(90)
    end_fill()

    dibujarAnterior()
    dibujarSiguiente()

def dibujarAnterior():
    restablecerTurtle()
    penup()
    color("red")
    goto(-330,-70)
    pendown()
    begin_fill()
    left(90)
    forward(50)
    left(120)
    forward(50)
    end_fill()

def dibujarSiguiente():
    restablecerTurtle()
    penup()
    color("red")
    goto(330,-70)
    pendown()
    begin_fill()
    left(90)
    forward(50)
    right(120)
    forward(50)
    end_fill()


def mostrarCuento(cuento):
    print(cuento)
    restablecerTurtle()
    penup()
    goto(-370, -230)
    write(cuento, align= "left", font=("arial", 14, "normal"))

        
def establecerNombreYEdad(nombre, edad, color,contadorPasos):
    
    global miListaCuento 
    miListaCuento = cuento(nombre, edad)
    mostrarCuento(miListaCuento[contadorPasos])
    dibujarFuncion(0, "red")


def clicPaso(x,y):
    global contadorPasos
   
    if (x >= 320 and x <= 380) and (y <= -10 and y >= -88): 
        rectanguloTexto()
        if contadorPasos < 4: 
            contadorPasos += 1
        mostrarCuento(miListaCuento[contadorPasos])
        dibujarFuncion(contadorPasos, "blue")

    elif (x >= -380 and x <= -320) and (y <= -10 and y >= -80):
        rectanguloTexto()
        if contadorPasos > 0:
            contadorPasos -= 1
            mostrarCuento(miListaCuento[contadorPasos])
            dibujarFuncion(contadorPasos, "blue") 
 
    else:
        print("no se preciono ningun boton")
