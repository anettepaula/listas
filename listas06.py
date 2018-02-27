#coding: utf-8
x = int(input("Digame cuantas palabras tiene la lista: "))
while x<0 :
	x = int(input("¡Imposible! Pruebe otra vez: "))
lista = []
reves = []

for i in range(x):
	palabra = raw_input("Digame la palabra "+str(i+1)+": ")
	lista += [palabra]
print "La lista creada es:",lista 
for i in(lista):
	reves.insert(0,i)
print "La lista inversa es:",reves
