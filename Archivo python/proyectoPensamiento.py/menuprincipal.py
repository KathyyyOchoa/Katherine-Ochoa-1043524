from turtle import *
from funcionesaux import *

ventana = Screen()

ventana.title("La feliz vida de arbolin")
ventana.setup(width=800, height=600)
ventana.bgcolor(("lightgrey"))
speed(0)
#hideturtle()

rectanguloDibujo()
rectanguloTexto()
dibujarCuadros()



nombre = textinput("Entrada de Nombre", "Ingresa tu nombre")
edad = textinput("Entrada de numero", "Ingresa tu edad")
color = textinput("Entrada de numero", "Selecciona tu color favorito: \n1. Rojo \n2. Amarillo \n3. Verde \n4. Rosado \n5. Azul")

establecerNombreYEdad(nombre, edad, color,0)

onscreenclick(clicPaso)

ventana.mainloop()






