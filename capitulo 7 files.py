#CAPITULO 7 "FILES"
#cosa = 'hola \nMundo!'
#print(cosa)

#entonces, para procesar datos y files
#para contar las lineas totales de un archivo
#fhand = open('loquesea')
#count = 0
#for line in fhand:
#    count = count+1
#print ('Conteo de lineas: ', count)

#para saber la cantidad de caracteres en un archivo
#fhand = open('mbox-short.txt')
#inp = fhand.read()
#print(len(inp))
#esto imrpimiría la cantidad de caracteres en el archivo, len() me entrega la cantidad de un objeto

#para encontrar algo en especifico a traves de un archivo, un correo por ejemplo
#fhand = open('mbox-short.txt')
#for line in fhand:
#   line = line.rstrip()
#   if line.startswith('From: '):
#       print(line)
#Y saldría algo tipo: From:qwerty@gmail.com

#Escribe un programa que solicite el nombre de un archivo, luego abra ese archivo y lo lea completamente, e imprima el contenido del 
# archivo en mayúsculas. Usa el archivo words.txt para producir la salida que se muestra abajo.
#Puedes descargar los datos de ejemplo en: http://www.py4e.com/code3/words.txt

## Use words.txt as the file name
#fname = input("Enter file name: ")
#fh = open(fname)
#for line in fh:
#    line = line.rstrip()        
#    print(line.upper())

#Escribe un programa que pida el nombre de un archivo, luego abra ese archivo y lo lea completamente, buscando líneas con el siguiente 
# formato:
#X-DSPAM-Confidence:    0.8475
#Cuenta estas líneas y extrae los valores de tipo decimal (float) de cada una de ellas, y calcula el promedio de esos valores para 
# producir una salida como la que se muestra abajo. No uses la función sum() ni una variable llamada sum en tu solución.
#Puedes descargar los datos de ejemplo en: http://www.py4e.com/code3/mbox-short.txt
#Cuando estés probando, escribe mbox-short.txt como nombre del archivo.

#fname = input("Enter file name: ")
#fh = open(fname)
#conteo = total = 0
#for line in fh:
#    if line.startswith("X-DSPAM-Confidence:"):
#        numero = float(line.split(':')[1]) #hasta acá capturo bien los números
#        if numero > 0:
#            conteo = conteo+1
#        total = total+numero
#prom = total/conteo
#print ('Average spam confidence:',prom )