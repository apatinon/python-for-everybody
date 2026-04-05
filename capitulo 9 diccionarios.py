#tradicionalmente tenemos, por ejemplo:
#cartas = list()
#cartas.append(12)
#cartas.append(3)
#cartas.append(75)
#print(cartas)
#cartas[1] = cartas[1]+2
#print(cartas)

#con un diccionario queda algo así
#cabinete = dict()
#cabinete['verano'] = 12
#cabinete['primavera'] = 3
#cabinete['invierno'] = 27
#print(cabinete)
#cabinete['primavera'] = cabinete['primavera']+2
#print(cabinete)
#el punto es que se guardan de la manera que yo neesite

#un ejemplo de recuento con diccionarios
#ccc = dict()
#ccc['lola']=1
#ccc['illojuan']=1
#print(ccc)
#ccc['lola']=ccc['lola']+1
#print(ccc)
#si tuvieramos muchos nombres podriamos pedirle que lea, por ejemplo linea por linea y me va a decir los valores que encuentra según el 
# nombre que yo le haya puesto, facilito pa

#conteo=dict()
#nombres=['juan', 'felipe', 'rodrigo', 'felipe', 'juan', 'juan' ]
#for nombre in nombres:
#    if nombre not in conteo:
#        conteo[nombre] = 1
#    else:
#        conteo[nombre]= conteo[nombre]+1
#print(conteo)

#y hay una vaina que se llama get() y lo que hace es dar un valor de 0 cuando la key todavía no está en el diccionario
#conteo=dict()
#nombres=['juan', 'felipe', 'rodrigo', 'felipe', 'juan', 'juan' ]
#for nombre in nombres:
#        conteo[nombre] = conteo.get(nombre, 0)+1
#print(conteo)

#Escribe un programa que lea el archivo mbox-short.txt y determine quién ha enviado la mayor cantidad de correos electrónicos. El 
# programa busca las líneas que comienzan con "From " y toma la segunda palabra de esas líneas como la persona que envió el correo.
#El programa crea un diccionario en Python que asigna la dirección de correo del remitente a la cantidad de veces que aparece en el 
# archivo.
#Después de construir el diccionario, el programa recorre sus elementos usando un bucle maximum para encontrar al remitente más 
# frecuente.

name = input("Enter file:")
fh = open(name)
correos = dict()

for line in fh:
    if line.startswith('From '):
        correo = line.split()[1]
        correos[correo] = correos.get(correo, 0)+1
mayor = max(correos, key=correos.get)
print(mayor, correos[mayor])