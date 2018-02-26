#coding: utf-8
x = int(input("Diagme cuantas palabras tiene la lista: "))
while x<=0 :
	x = int(input("¡Imposible! Pruebe otra vez: "))
a = []
for i in range(x):
	palabra = raw_input("Dígame la palabra "+str(i+1)+": ")
	a += [palabra]
print "La lista creada es",a
fuera = raw_input("Palabra a eliminar: ")

for i in range(a.count(fuera)) :
	a.remove(fuera)

print a
	
