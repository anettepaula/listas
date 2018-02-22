#coding: utf-8
x = int(input("Diagme cuantas palabras tiene la lista: "))
while x<=0 :
	x = int(input("¡Imposible! Pruebe otra vez: "))
a = []
for i in range(x) :
	palabra = raw_input("Digame la palabra "+str(i+1)+": ")
	a += [palabra]
print "La lista creada es",a
pala = raw_input("Digame la palabra a buscar: ")
print "La palabra",pala,"aparece",a.count(pala),"veces en la lista."
