#coding: utf-8
num = int(input("Digame cuantas palabras tiene la lista: "))
while num<0:
	num = int(input("Error. Pruebe otra vez: "))
primera = []
for i in range(num):
	palabra= raw_input("Digame la palabra "+str(i+1)+": ")
	primera += [palabra]
print "La lista creada es:",primera
for i in (primera):
	if (primera.count(i)>1) :
		primera.remove(i)
print "La lista sin repeticiones es: ", primera

for i in range(len(primera)-1,-1,-1):
	if (primera.count(i)>1) :
		primera.remove(i)
print primera

