#coding: utf-8
x = int(input("Diagme cuantas palabras tiene la lista: "))
while x<=0 :
	x = int(input("¡Imposible! Pruebe otra vez: "))
a = []
for i in range(x):
	palabra = raw_input("Dígame la palabra "+str(i+1)+": ")
	a += [palabra]
print "La lista creada es:",a
primera=raw_input("Sustituir la palabra: ")
segunda=raw_input("por la palabra: ")

for i in range(a.count(primera)):
	no = a.index(primera)
	a[no]=segunda

print "La lista es ahora",a

