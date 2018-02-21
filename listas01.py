#coding: utf-8
x = int(input("Digame cuantas palabras tiene la lista: "))
while x<=0 :
	x = int(input("¡Imposible! Pruebe otra vez: "))
else : 
	a = []
	for i in range(x) :
		palabra = raw_input("Digame la palabra "+str(i+1)+": ")
		a += [palabra]
print "La lista es",a
		


