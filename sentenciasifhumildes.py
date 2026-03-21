#mi idea es empezar a organizar los ejecicios en un solo archivo .py para
#que sea más fácil acceder y organizar esta información en el github
def ejercicio1():
    print("Está corriendo el ejercicio 1") 
    #Escribe un programa que le pida al usuario las horas trabajadas y la tarifa por hora usando input para calcular el salario bruto. Paga
    #la tarifa normal por las horas hasta 40, y 1.5 veces la tarifa por hora por todas las horas trabajadas por encima de 40. Usa 45 
    #horas y una tarifa de 10.50 por hora para probar el programa (el salario debería ser 498.75).
    #Debes usar input para leer una cadena de texto y float() para convertir esa cadena en un número.
    #No te preocupes por validar errores en la entrada del usuario; asume que el usuario ingresa los números correctamente.
    horas = input("ingrese la cantidad de horas laburadas: ")
    hrs = float(horas)
    salariotexto = input("ingrese la cantidad de dinero que se paga por hora laburada ")
    salario = float(salariotexto)
    if hrs<=40: 
        pago = hrs*salario
        print (pago)
    else: 
        hextra = float(hrs-40)
        pago = (hextra*1.5*salario)+salario*40
        print (pago)

def ejercicio2():
    print("Está corriendo el ejercicio 2") 

seleccion = int(input("Escriba el número del programa que quiere ejecutar " ))
if seleccion == 1:
    ejercicio1()
elif seleccion ==2:
    ejercicio2()    
