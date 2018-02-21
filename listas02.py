#coding: utf-8
x = int(input("Diagme cuantas palabras tiene la lista: "))
while x<=0 :
	x = int(input("¡Imposible! Pruebe otra vez: "))
else : 
	a = []
	for i in range(x) :
		palabra = raw_input("Digame la palabra "+str(i+1)+": ")
		a += [palabra]
print "La lista creada es",a
pala = raw_input("Digame la palabra a buscar: ")
si = pala in a
if si == "True" :
	print "hr"
else : 
	print "aaa"
