#CAPITULO 4: FUNCIONES: ejemplos y ejercicios de esta sección

#primer ejemplo simple mostrado en el curso 
#def greet(lang):
# if lang == 'es':
#  print('hola')
# elif lang == 'fr':
#  print('bonjour')
# else:
#  print('hello')

#segundo ejemplo simple mostrado en el curso
#def addtwo(a, b):
#    added = a + b
#    return added
#x = addtwo(3, 5)
#print(x) 

#escriba un programa que le pida al usuario las las horas trabajadas y la tarifa por hora usando input, para calcular el pago bruto.
#el pago debe ser: la tarifa normal para las horas hasta 40 y "tiempo y medio" para todas las horas trabajadas por encima de 40. 
#la logica del calculo debe ponerse dentro de una funcion llamada computepay() y use esa funcion para hacer el calculo. La funcion 
#debe retornar un valor. Testee con 45 horas y tarifa de 10.50 por hora para probar el programa
def computepay(h, r):
    if h>40:
        hextra = float(h-40)
        p = (hextra*1.5*r)+r*40
    else: p = h*r 
    return p

h = float(input("Ingrese las horas: "))
r = float(input("Ingrese el ratio: "))
p = computepay(h, r)
print("pago : ", p)