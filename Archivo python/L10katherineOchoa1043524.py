#KatherineOchoa1043524

print("semana No. 10: ejercicio 1")

mesEntrada = int(input("ingrese un numero del 1-12"))

match mesEntrada:
    case 1:
        mesSalida = "Enero"
    case 2:
        mesSalida = "Febrero"
    case 3: 
        mesSalida = "Marzo"
    case 4: 
        mesSalida = "abril"
    case 5:
        mesSalida = "mayo"
    case 6:
        mesSalida = "junio"
    case 7:
        mesSalida = "julio"
    case 8:
        mesSalida = "agosto"
    case 9: 
        mesSalida = "sepyiembre"
    case 10:
        mesSalida = "otubre"
    case 11:
        mesSalida = "noviembre"
    case 12:
        mesSalida = "diciembre"
    case _:
        print("error: el numero a ingresar debe estar contenido entre 1")

print(mesSalida)

#Actividad 2
print("semana No. 10: Ejercicio 2")

#entradas 

a = int(input("ingrese el primer numero mayor a cero"))
b = int(input("ingrese el segundo numero mayor a cero"))
c = int(input("ingrese el tercer numero mayor a cero"))

#validacion
if(a <= 0 or c <= 0):
    print("Error: el numero debe ser mayor a cero")

#diagrama 
print("el numeros es")
if(a>b):
    if(a>b):
        print(a)
    else: 
        if (a == c):
            print(a, "y", c)
        else: 
            print(c)
elif( a ==b ):
    if(a > b): 
        print(a, b)
    elif (a == c):
        print(a, b, c)
else:
    print(c)
if (b>c):
    print(c)
elif (b == c):
    print(b, "y",c)
else:
    print(c)

#signos sodiacales
    d = int(input("Ingrese su día de nacimiento "))
m = int(input("Ingrese su mes de nacimiento "))
a = int(input("Ingrese su año de nacimiento "))
z= ""

match m:
    case 1:
        if (d<=19):
            print("Capricornio")
        else: 
            print("Acuario")
    case 2:
        if (d<=18):
            print("Acuario")
        else: 
            print("Piscis")
    case 3:
        if (d<=20):
            print("Piscis")
        else: 
            print("Aries")
    case 4:
        if (d<=19):
            print("Aries")
        else: 
            print("Tauro")
    case 5:
        if (d<=20):
            print("Tauro")
        else: 
            print("Géminis")
    case 6:
        if (d<=20):
            print("Géminis")
        else: 
            print("Cáncer")
    case 7:
        if (d<=22):
            print("Cáncer")
        else: 
            print("Leo")
    case 8:
        if (d<=22):
            print("Leo")
        else: 
            print("Virgo")
    case 9:
        if (d<=22):
            print("Virgo")
        else: 
            print("Libra")
    case 10:
        if (d<=22):
            print("Libra")
        else: 
            print("Escorpio")
    case 11:
        if (d<=21):
            print("Escorpio")
        else: 
            print("Sagitario")
    case 12:
        if (d<=21):
            print("Sagitario")
        else: 
            print("Capricornio")




    