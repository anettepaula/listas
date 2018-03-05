#coding: utf-8
num = int(input("Digame cuantas palabras tiene la primera lista: "))
while num<0:
	num = int(input("Error. Pruebe otra vez: "))
primera = []

for i in range(num):
	palabra1 = raw_input("Digame la palabra "+str(i+1)+": ")
	primera += [palabra1]
print "La primera lista es:",primera

segunda = []

num2 = int(input("Digame cuantas palabras tiene la segunda lista: "))
while num2<0:
	num2 = int(input("Error. Pruebe otra vez: ")) 

for i in range(num2):
	palabra2 = raw_input("Digame la palabra "+str(i+1)+": ")
	segunda += [palabra2]

print "La segunda lista es:",segunda

listas2 = []

for i in (segunda):
	if (primera.count(i)>0):
		listas2 += [i]
print "Palabras que aparecen en ambas listas",listas2
lista1 = []
for i in (primera):
	if i not in (segunda):
		lista1 += [i]
	
print "Palabras que solo aparecen en la primera lista:", lista1
lista2= []
for i in (segunda):
	if i not in (primera):
		lista2 += [i]

print "Palabras que solo aparecen en las segunda lista:",lista2

todas = lista1 + lista2

print "Todas las palabras",todas

	
	
