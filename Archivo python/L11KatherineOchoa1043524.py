print("semana No.11:ejercicio 1")

n = int(input("ingrese un numero mayor a 0"))

#declaracion de variables
a = 0
b = 1
c = 0
i = 2
resultado = ""

if (n>0):
    resultado = str(a)

    if(n>1):
        resultado += " , " + str(b)
    while(i<n):
         c = a + b
         resultado += " , " + str(c)
         a = b = c
         i = i + 1 

    print(resultado)
else: 
    print(resultado)

#Ejercicio 2
print("semana No.11:ejercicio 2") 

n = int(input("ingrese un numero mayor a 0"))

if(n <= 0):
    print("Error: el numero debe ser mayor a cero")

resultadoA = 0
for x in range (1, n+1):
    resultadoA += (1/x)
    print("Inciso A:", resultadoA)

#Ejercicio 3
        
    

