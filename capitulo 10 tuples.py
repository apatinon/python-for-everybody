#ultimo capitulo del curso, se ven tuples
#d = {'b':10, 'c':33, 'a':10}
#t = sorted(d.items()) 
#print(t)
#for k, v in sorted(d.items()):
#    print(k, v)

#c = {'a':10, 'b':1, 'c':22}
#tmp = list()
#for k, v in c.items():
#    tmp.append((v, k))
#print(tmp)
#tmp = sorted(tmp, reverse= True)
#print(tmp)

#una manera muchisisisimo más compacta de hacerlo
#print(sorted([( v,k ) for k,v in c.items()]))

#Escribe un programa que lea el archivo mbox-short.txt y determine la distribución por hora del día de cada uno de los mensajes.
#Puedes extraer la hora de las líneas que comienzan con "From " encontrando la hora y luego separando la cadena una segunda vez usando 
# los dos puntos (:).
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Una vez que hayas acumulado la cantidad de mensajes para cada hora, imprime los conteos ordenados por hora como se muestra a continuación.

name = input("Enter file:")
fh = open(name)
tmp = dict()
for line in fh: 
    if line.startswith('From '):
        horams = line.split()[5]
        hora = horams.split(':')[0]
        tmp[hora] = tmp.get(hora, 0)+1
for k, v in sorted(tmp.items()):
    print(k, v)