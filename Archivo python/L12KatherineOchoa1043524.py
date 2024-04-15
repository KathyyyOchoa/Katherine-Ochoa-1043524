print("Semana No.12: ejercicio 1")

print("a. sumatoria","b. factorial","c. tablas de multiplicar","d. numero perfecto")

opcion = input("Ingrese la letra de su opcion:")

match opcion:
    case "a":
        n = int(input("ingrese un numero entero positivo"))

        if(n > 0):
           sumatoria = 0;
           i = 1
           while(i <= n):
               sumatoria = sumatoria + i;
               i = i =1 
           print("sumatoria es:", sumatoria)
        else: 
            print("Error, el numero debe ser mayor a cero")
    case "b":
         n = int(input("ingrese un numero entero positivo"))
         if(n > 0):
           factorial = 0;
           i = 1
           while(i <= n):
               factorial = factorial + i;
               i = i +1 
           print("sumatoria es:",factorial)
    case "c":
        tituloColumnas = "\t"

        for i in range(1 , 11):
            tituloColumnas = tituloColumnas + str(i) + "\t"
        print(tituloColumnas)

        for filas in range(1 , 11):
         cadenaFila = str(filas) + "\t"
         for columnas in range(1 , 11):
             cadenaFila = cadenaFila + str(filas * columnas)+ "\t"
         print(cadenaFila) 
    case "d":
        int(input("Ingrese un número entero: "))
for i in range(2, i+1):
    b=0
    for j in range(1, (i//2)+1):
        if((i%j)==0):
            b= b+j
    if(b==i):
        print("%s es perfecto" %i)
    else:
        print("%s no es perfecto" %i)

         