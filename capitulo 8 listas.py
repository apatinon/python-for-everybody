#puedo manipular las listas como ya se ha mostrado en capitulos anteriores y hay funciones que son para ellas casi que especificamente, len, range, etc

#por ejemplo puedo crear una lista vacía y llenarla con inputs que le pido al usuario:
#listanum = list()
#while True:
#    inp = input('ingrese un numero: ')
#    if inp == 'listo' : break
#    value = float(inp)
#    listanum.append(value)
#promedio = sum(listanum) / len(listanum)
#print('promedio: ', promedio)

#las listas tambien pueden tener o ser de strings
#abc = 'con tres palabras'
#vaina = abc.split() #esto crea una lista
#type(abc)
#print(vaina)
#print(vaina[0])
#for x in vaina:
#    print(x)

#line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
#words = line.split()
#email = words[1]
#pieces = email.split('@')
#print(email)
#print(pieces)

#Abre el archivo romeo.txt y léelo línea por línea.
#Para cada línea, divídela en una lista de palabras usando el método split().
#El programa debe construir una lista de palabras.
#Para cada palabra en cada línea, verifica si la palabra ya está en la lista y, si no lo está, agrégala a la lista.
#Cuando el programa termine, ordena e imprime las palabras resultantes en orden alfabético usando sort() o como se muestra en la salida deseada.
#Puedes descargar los datos de ejemplo en: http://www.py4e.com/code3/romeo.txt

#SOLUCION
#fname = input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
#    words = line.split()
#    for word in words:
#        if word not in lst:
#            lst.append(word)
#lst.sort()        
#print(lst)

#Abre el archivo mbox-short.txt y léelo línea por línea. Cuando encuentres una línea que empiece con 'From ', como la siguiente:

#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#Deberás analizar (parsear) la línea usando split() y mostrar la segunda palabra de la línea (es decir, la dirección completa de la 
# persona que envió el mensaje).
#Luego, imprime un conteo al final.
#Pista: asegúrate de no incluir las líneas que empiezan con 'From:'. También mira la última línea de la salida de ejemplo para ver cómo 
# imprimir el conteo.
#Puedes descargar los datos de ejemplo en:
#http://www.py4e.com/code3/mbox-short.txt

fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From "):
        renglon = line.split()
        count = count+1
        print(renglon[1])
print('There were', count, 'lines in the file with From as the first word')

