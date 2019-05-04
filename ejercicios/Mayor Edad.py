# -*- coding: utf-8 -*-
"""
Created on Sat May  4 09:01:11 2019

@author: android
"""

print("Digite Edad")
edad = input()
edad = int(edad)
if edad >= 18:
    print('Es Mayor de Edad')
else:
    print('Es Menor de Edad')

# si de linea con sino
print('Es Mayor de Edad') if edad >= 18 else print('Es Menor de Edad')

v = ["Hola", "Mundo", 4, 3.4, True, ["Otro", "Array", "Dentro"]]

v2 = ["Hola", "Mundo"]

v3 = range(10)

v4 = range(200)

for x in v4:
    print(x)

print(v2[0])

# Eliminar elementos

v2.remove("Hola")

# Eliminar el ultimo elemento

v.pop()

# agregar elemento
v.append(5)
v.insert(1, "Daniel")

# borrar todo el vector
v.clear

# numero de elementos de un array

len(v)

# cuantas veces aparece un elemento en el vector

v.count('Mundo')

# ordenar un vector

a = [5, 9, 6, 7, 11]
a.sort()

# a = a.sort()

5 in a

# recorrer un vector

# for x in v
    


print("Digite Hasta")
a = int(input())
suma = 0
for x in range(a+1):
    suma = suma + x
print("La sumatoria es: ",suma)