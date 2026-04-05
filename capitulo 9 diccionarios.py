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