#coding: utf-8
x = int(input("Diagme cuantas palabras tiene la lista: "))
while x<=0 :
	x = int(input("¡Imposible! Pruebe otra vez: "))
a = []
b = []
for i in range(x):
	palabra = raw_input("Dígame la palabra "+str(i+1)+": ")
	a += [palabra]
print "La lista creada es:",a
y = int(input("Dígame cuántas palabras tiene la lista de palabras a eliminar: "))

for i in range(y):
	eliminar = raw_input("Dígame la palabra "+str(i+1)+": ")
	b += [eliminar]

print "La lista de palabras a eliminar es:",b
a+b
print b
print a
