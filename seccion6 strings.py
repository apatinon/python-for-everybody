#fruit = 'banano'
#letter = fruit[1]
#print(letter)
#letter = fruit[2]
#print(letter)
#letter = fruit[5]
#print(letter)
#x=3
#w=fruit[x-1]
#print(w)

#palabra = 'banana'
#count = 0
#for letter in palabra:
#    if letter == 'a':
#        count=count+1
#    print(count)

#s='Monty Python'
#print(s[6:7])
#print(s[0:4])
#print(s[6:20])
#print(s[:2])
#print(s[8:])
#print(s[:])

#IN COMO OPERADOR LÓGICO
#fruit = 'banano'
#letra = input('ingrese la letra que quiere buscar en banano:')
#if letra in fruit:
#    print('si está')
#else: 
#    print('no está')

#BUSQUEDA Y REEMPLAZO   
#jum = "Hola andres"
#nstr= jum.replace('andres','felipe')
#print(nstr)
#nstr= jum.replace('a','X')
#print(nstr)

#UN EJEMLPO QUE MEZCLA ALGUNAS COSAS CON UN CORREO
#data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
#atpos = data.find('@')
#print(atpos)
#sppos = data.find(' ',atpos)
#print(sppos)
#host = data[atpos+1 : sppos]
#print(host)

text = "X-DSPAM-Confidence:    0.8475"
numero = text.find('0')
print(float(text[23:100]))
