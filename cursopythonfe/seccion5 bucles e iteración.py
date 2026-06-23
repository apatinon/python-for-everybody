#primer ejemplo de esta sección que usa solo "while"
#n = float(input("ingrese el inicio de su cuenta regresiva: "))
#while n > 0:
#    print(n)
#    n = n-1
#print('BOOOOOOM!!')

# ahora haremos algo parecido a lo de arriba pero con "for" y "in"
#for i in [5 , 4, 3, 2, 1]:
#    print(i)
#print('CATAPLASSSSS!!!')

#También funciona con str
#amigos = ['lucho', 'juancho', 'Bryan']
#for amigo in amigos:
#    print('Feliz año: ', amigo)
#print('Listos')

#este ejemplo sirve para encontrar el mayor en una lista de números,
#el punto es que elnumero y elmasgrande cambian constantemente por 
#esa condición if que estamos usando:
#elmasgrande = -1
#for elnumero in [5, 64, 21, 17, 82, 37]:
#    if elnumero > elmasgrande:
#        elmasgrande = elnumero
#    print(elmasgrande, elnumero)

#un ejemplito de como contar en un bucle, asigna un numero a cada elemento de la lista y luego me da el total de elementos que tienen algo asignado
#jum = 0
#print('antes', jum)
#for puchaina in [3, 64, 2, 67, 13, 85]:
#    jum = jum+1
#    print(jum, puchaina)
#print('Después', jum)

#esta humilde secuencia nos muestra la cantidad de numeros de la secuencia de fibnoaci que el usuario quiera
#n = 0
#m = 1
#z = int(input('ingrese la cantidad de números que quiere de la secuencia de:'))
#for i in range(z):
#    print(n)
#    n = m
#    m = n+m

#podemos usar una variable booleana para encontrar un elemento en un conjunto
#analisis = False
#print('Antes', analisis)
#for i in [4, 68, 12, 53, 49, 50]:
#    if i ==12:
#        analisis = True
#    print(analisis, i)

#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out 
# the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put 
# out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.


masgrandre= int(-1)
maspequeño= None
while True:
    entrada = input("ingrese un numero: ")
    if entrada == "done":
        break
    try:
        num = int(entrada)
    except:
        print("invalid input")
        continue
    num = int(entrada)
    if num>masgrandre:
            masgrandre=num
    elif maspequeño is None:
            maspequeño=num
    elif maspequeño<num:
            maspequeño=num
print("Maximum is", masgrandre)
print("Minimum is", maspequeño)
